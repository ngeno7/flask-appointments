let mix = require('laravel-mix');

mix.js('src/app.js', 'js').setPublicPath('appointments/static').vue({ version: 3 });
