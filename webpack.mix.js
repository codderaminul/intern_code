const mix = require('laravel-mix');


mix.react('src/templates/assets/js/app.js', 'src/static/js')
    .sass('src/templates/assets/scss/main.scss', 'src/static/css');