# URL Shortener

## Description

This Python script provides a simple URL shortening functionality using the TinyURL API. It takes a long (big) URL as input and returns a shortened URL that redirects to the original URL.

## How It Works

1. The script imports the `post` method from the `requests` module, which is used to send HTTP requests.

2. It defines a function `TinyShortner(big_url)`, which takes a single argument `big_url` (the long URL to be shortened).

3. Inside this function, it sends a POST request to the TinyURL API with the long URL as data. The API responds with a shortened URL, which is then returned by the function.

4. If the script is run as the main module, it prompts the user to input a long URL, then passes this URL to the `TinyShortner` function.

5. The shortened URL is then printed to the console.
