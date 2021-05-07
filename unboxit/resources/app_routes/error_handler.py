from flask import render_template


class ErrorHandler():
    """
        Generic class for handling errors server errors.
        These methods are registered in the root of this folder
        __init__.py
    """
    def page_not_found(e):
        """
            Handle 404 errors.
        """
        return render_template('components/404.html'), 404

    def internal_error(e):
        """
            Handle 500 errors.
        """
        return render_template('components/500.html'), 500
