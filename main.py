file_metadata = {'name': 'file.csv'}
media = MediaFileUpload('file.csv',
                        mimetype='text/jpeg')
file = drive_service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
print 'File ID: %s' % file.get('id')


