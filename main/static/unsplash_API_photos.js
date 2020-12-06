function unsplash_API_images() {
    $.getJSON('static/unsplash_images.json', function(data) {
        // add images in the boxes (main page)
        $('.left_box img').attr('src', data[10].urls.regular);
        $('.left_box img').attr('alt', data[10].alt_description);

        $('.right_box img').attr('src', data[7].urls.regular);
        $('.right_box img').attr('alt', data[7].alt_description);
    });
}
unsplash_API_images()