# coding=utf-8
import re
import uuid
import requests
import ntpath
import mimetypes
from io import BytesIO
from tempfile import NamedTemporaryFile

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client


# 10 years
DEFAULT_EXPIRE_TIME = 60 * 60 * 12 * 365 * 10 
DEFAULT_QCLOUD = {
    'secret_id': 'AKIDjOTO9qnlxyoBe2aJB2vmTzKVYVL5m6NT',
    'secret_key': '65t0xlYEnCQn2771nR3Ys18A2oT3Yy31',
    'region': 'ap-beijing',
}

class BaseUploader(object):
    def upload_from_url(self, url):
        try:
            filename = re.findall('.*/(\S+)\??', url)[0]
            prefix=filename.split('.')[0]
            suffix=filename.split('.')[1] 
        except Exception, e:
            filename = str(uuid.uuid4())
            prefix=filename
            suffix=None

        f = NamedTemporaryFile(delete=True, suffix=suffix, prefix=prefix)
        res = requests.get(url)
        f.write(res.content)
        f.seek(0)

        download_filename = f.name
        url = self.upload_from_file(download_filename)
        f.close()
        return url

    def upload_from_file(self, filename):
        con = open(filename, 'r').read() 
        key = ntpath.basename(filename)
        return self._upload_from_stream(con, key)

    def _upload_from_stream(self, steam, filename):
        raise Exception("NOT SUPPORT")

class QCloudUploader(BaseUploader):
    @classmethod
    def from_default_config(cls):
        return cls(**DEFAULT_QCLOUD)

    def __init__(self, **kwargs):
        secret_id = kwargs['secret_id']
        secret_key = kwargs['secret_key']
        region = kwargs['region']
        config = CosConfig(Region=region, Secret_id=secret_id, Secret_key=secret_key, Token='')
        self.upload_client = CosS3Client(config)

    def _upload_from_stream(self, stream, filename):
        DEFAULT_MIME_TYPE = "application/octet-stream"
        try:
            mimetypes.init()
            content_type = mimetypes.types_map.get(".%s"%filename.split('.')[-1], DEFAULT_MIME_TYPE)
        except Exception, e:
            content_type = DEFAULT_MIME_TYPE

        #generate a random uuid
        #althougt key is same
        #but get two diff url
        object_key = "%s"%(str(uuid.uuid4()))

        bucket = self._generate_bucket(object_key)
        #TODO setting content-type
        response = self.upload_client.put_object(
            Bucket=bucket,
            Body=stream,
            Key=object_key,
            StorageClass='STANDARD',
            CacheControl='no-cache',
            ContentDisposition=file
        )
        if response:
            uploaded_url = self._generate_public_url(object_key, DEFAULT_EXPIRE_TIME)
            return uploaded_url
        return None

    def _generate_bucket(self, key):
        BUCKET_SIZE = 16 
        bucket = "img-prod-{:0>3d}-1255633922".format(hash(key) % BUCKET_SIZE + 1)
        return bucket 

    def _generate_public_url(self, key, expired):
        bucket = self._generate_bucket(key)
        return self.upload_client.get_presigned_download_url(bucket, key, expired)

if __name__ == "__main__":
    upr = QCloudUploader.from_default_config()
    org_url = "https://www.microsoft.com/zh-hk/CMSImages/WindowsHello_Poster_1920-1600x300-hello.png?version=0d8f51c7-ef87-b0af-8f26-453fb40b4b7d"
    new_url = upr.upload_from_url(org_url)
    print new_url
    assert new_url
    assert org_url != new_url
    assert "myqcloud.com" in new_url