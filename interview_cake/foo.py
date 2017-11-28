import os
import hashlib


def find_duplicate_files(starting_directory='/tmp/test'):
    files_seen_already = {}
    queue = [starting_directory]

    duplicates = []

    while len(queue) > 0:
        current_path = queue.pop()

        # if it's a directory
        # put the contents in our queue
        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                full_path = os.path.join(current_path, path)
                queue.append(full_path)
        # if it's a file:
        else:
            file_hash = sample_hash_file(current_path)
            current_last_edited_time = os.path.getmtime(current_path)

            # if we've seen in before
            if file_hash in files_seen_already:
                existing_last_edited_time, existing_path = files_seen_already[file_hash]

                if current_last_edited_time > existing_last_edited_time:
                    # current file is the dupe
                    duplicates.append((current_path, existing_path))
                else:
                    # old file is the dupe
                    duplicates.append((existing_path, current_path))

                    # but also update the hash to have the new file's info:
                    files_seen_already[file_hash] = (current_last_edited_time, current_path)
            # it's a new file
            else:
                files_seen_already[file_hash] = (current_last_edited_time, current_path)

    return duplicates



def sample_hash_file(path):
    num_bytes_to_read_per_sample = 4000
    total_bytes = os.path.getsize(path)

    hasher = hashlib.sha512()

    with open(path, 'rb') as file:

        # first bytes
        sample = file.read(num_bytes_to_read_per_sample)
        hasher.update(sample)

        # middle bytes
        file.seek(total_bytes / 2)
        sample = file.read(num_bytes_to_read_per_sample)
        hasher.update(sample)

        if total_bytes > num_bytes_to_read_per_sample * 3:
            file.seek(-num_bytes_to_read_per_sample, os.SEEK_END)
            sample = file.read(num_bytes_to_read_per_sample)
            hasher.update(sample)

    return hasher.hexdigest()

print find_duplicate_files("/Users/alagram/Documents/Dev/interview_cake")
