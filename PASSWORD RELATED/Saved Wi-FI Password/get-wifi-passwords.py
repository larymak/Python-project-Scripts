import os
import platform
import subprocess


def get_all_profiles():
    system = platform.system()
    if system == 'Windows':
        try:
            data = subprocess.check_output(
                ["netsh", "wlan", "show", "profiles", "key=clear"]
            ).decode("utf-8", errors="backslashreplace")
            return data
        except subprocess.CalledProcessError as error:
            return f"Error: {error}"
    else:
        return "Only For Windows"


def get_profiles_info(profile):
    system = platform.system()
    if system == 'Windows':
        try:
            data = subprocess.check_output(
                ["netsh", "wlan", "show", "profiles", profile, "key=clear"]
            ).decode("utf-8", errors="backslashreplace")
            return data
        except subprocess.CalledProcessError as error:
            return f"Error: {error}"
    else:
        return "Only For Windows"


def output_to_file(file_path, data):
    with open(file_path, 'w') as f:
        f.write(data)


def delete_profile(profile):
    system = platform.system()
    if system == 'Windows':
        try:
            subprocess.check_call(
                ["netsh", "wlan", "delete", "profile", f"name=\"{profile}\""]
            )
            return f"{profile} profile deleted successfully"
        except subprocess.CalledProcessError as error:
            return f"Error: {error}"
    else:
        return "Only For Windows"


if __name__ == "__main__":
    print("Fetching all saved Wi-Fi profiles...")
    profiles = get_all_profiles()
    print(profiles)

    if profiles != "Only For Windows":
        profile_name = input("Enter the profile name: ")
        profile_info = get_profiles_info(profile_name)
        print(profile_info)

        output_choice = input("Do you want to output the results to a file? (y/n): ")
        if output_choice.lower() == 'y':
            file_path = input("Enter the file path to save the output: ")
            output_to_file(file_path, profile_info)

        delete_choice = input("Do you want to delete this profile? (y/n): ")
        if delete_choice.lower() == 'y':
            delete_result = delete_profile(profile_name)
            print(delete_result)
