s3_bucket_list = ["siva-b0", "raju-b1", "raghu-b2", "rekha-b3", "nara-b4"]
s3_bucket_list.append ("raju-b1")
print(len(s3_bucket_list))


new_bucket = s3_bucket_list[1:4]
print(new_bucket)
print(len(new_bucket))

