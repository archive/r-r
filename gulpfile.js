'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('default', ['sass'], function () {

});

gulp.task('sass', function () {
	gulp.src('./src/static/styles/master.scss')
		.pipe(sass().on('error', sass.logError))
		.pipe(gulp.dest('./src/static/output'));
});

gulp.task('sass:watch', function () {
	gulp.watch('./src/static/styles/**/*.scss', ['sass']);
});