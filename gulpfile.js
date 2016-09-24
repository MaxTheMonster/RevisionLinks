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
        .pipe(browserSync.stream());
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
    gulp.watch('static/scss/*.scss'), ['css'];
    gulp.watch('static/js/*.js'), ['js'];
    gulp.watch('static/img/*.*'), ['img'];
});
