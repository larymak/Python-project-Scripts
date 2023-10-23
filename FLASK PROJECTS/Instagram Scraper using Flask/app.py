from flask import Flask, request, jsonify
from helper import get_all_posts, scrape_user_id
import instaloader

app = Flask(__name__)
insta = instaloader.Instaloader()

@app.route('/', methods=['GET'])
def start():
    return "Instragram Scraper Server is Running!!"

@app.route('/get_profile/<username>', methods=['GET'])
def get_instagram_profile(username):
    try:
        profile = instaloader.Profile.from_username(insta.context, username)
        #Get 
        user_id = scrape_user_id(username)
        # Get post data for all posts
        post_data = get_all_posts(user_id)
        response = {
            "Username": profile.username,
            "Number Of Posts": profile.mediacount,
            "Posts": post_data
        }
        return jsonify(response)
    except instaloader.exceptions.ProfileNotExistsException:
        return jsonify({"error": "Profile does not exist"}), 404
    except instaloader.exceptions.InstaloaderException as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"{str(e)}"}), 400


if __name__ == '__main__':
    app.run()
