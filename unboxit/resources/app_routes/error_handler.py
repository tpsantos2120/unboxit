from flask import render_template


class ErrorHandler():
    def page_not_found(e):
        return render_template('components/error_404.html'), 404

    def internal_error(e):
        return render_template('components/error_500.html'), 500
    
    def not_authorized(e):
        return render_template('components/error_401.html'), 401
