from storages.backends.gcloud import GoogleCloudStorage


storage = GoogleCloudStorage()


class Uploader:
    @staticmethod
    def image_upload(file, filename):
        try:
            target_path = 'images/' + filename
            path = storage.save(target_path, file)
            return storage.url(path)
        except Exception as e:
            print(e, "EXCEPTION")
