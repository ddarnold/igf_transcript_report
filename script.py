import os
import re

# Function to process each file
def process_file(file_path, log_file):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Log file name
    log_file.write(f"{file_path}:\n")

    # Log if the file does not contain <transcript> and </transcript> tags
    transcript_start = content.find("<transcript>")
    transcript_end = content.find("</transcript>")
    
    if transcript_start == -1 or transcript_end == -1:
        log_file.write("does not contain <transcript> and </transcript> tags.\n")
    else:
        # Check if there are any <speaker> tags outside the <transcript>...</transcript> block
        before_transcript = content[:transcript_start]
        after_transcript = content[transcript_end + len("</transcript>"):]
        
        speakers_before = re.findall(r'<speaker>(.*?)</speaker>', before_transcript)
        speakers_after = re.findall(r'<speaker>(.*?)</speaker>', after_transcript)
        
        if speakers_before or speakers_after:
            log_file.write(f"contains <speaker> tags outside <transcript>...</transcript> block: "
                           f"{'Before' if speakers_before else ''} "
                           f"{'Before and After' if (speakers_before and speakers_after) else ''} "
                           f"{'After' if speakers_after else ''}\n")

    # Count occurrences of ">>"
    count = content.count(">>")
    if count > 0:
        log_file.write(f"contain '>>':{count}\n")
    
    # Log if the file contain >MODERATOR speaker 
    if (">MODERATOR" in content):
        log_file.write("contain >MODERATOR\n")
        
    # Function to check if all tags are properly closed
    tags = re.findall(r'<[^>]*>', content)
    for i in range(len(tags) - 1):
        if not tags[i].endswith('>'):
            log_file.write(f"{file_path} contains improperly closed tags (some '<' tags are not followed by '>').\n")
    
    # Find all unique strings between <speaker> and </speaker> tags
    speakers = set(re.findall(r'<speaker>(.*?)</speaker>', content))
    if speakers:
        log_file.write(f"Speakers:{', '.join(speakers)}\n")

    log_file.write("\n")

# Main script to process all .txt files in the same folder
def process_folder(folder_path):
    log_path = os.path.join(folder_path, "log.txt")
    with open(log_path, 'w', encoding='utf-8') as log_file:
        # Get all files ending with .txt and sort them alphabetically
        txt_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".txt")])
        
        for filename in txt_files:
            file_path = os.path.join(folder_path, filename)
            process_file(file_path, log_file)

if __name__ == "__main__":
    folder_path = "."  # Replace with the path to your folder
    process_folder(folder_path)
