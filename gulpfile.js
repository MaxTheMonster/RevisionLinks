var gulp = require('gulp'),
    sass = require('gulp-sass'),
    cssminify = require('gulp-minify-css'),
    autoprefixer = require('gulp-autoprefixer'),
    uglify = require('gulp-uglify');

gulp.task('css', function() {
    gulp.src('static/scss/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(cssminify({compatibility: 'ie8'}))
        .pipe(autoprefixer({
            browsers: ['last 2 versions'],
            cascade: false
        }))

        .pipe(gulp.dest('static/css/'))
});

gulp.task('js', function() {
  gulp.src('static/js/*.js')
    .pipe(uglify())
    .pipe(gulp.dest('static/js'));
});

gulp.task('img', function() {
  gulp.src('static/img/*.*')
    .pipe(imageminOptipng({optimizationLevel: 3})())
    .pipe(gulp.dest('static/img'));
  });

gulp.task('default',function() {
    styles_watcher = gulp.watch('static/scss/*.scss', ['css']);
    styles_watcher.on("change", function(event) {
        console.log("Compiled some Scss!")
    });

    js_watcher = gulp.watch('static/js/*.js', ['js']);
    js_watcher.on("change", function(event) {
        console.log("Compiled some JS!")
    });

    img_watcher = gulp.watch('static/img/*.*', ['img']);
    img_watcher.on("change", function(event) {
        console.log("Optimized some images!")
    });
});
