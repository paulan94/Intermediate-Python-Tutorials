
##@app.route('/contact/')
##def contact(): #when function is called, use that contact template
##    return render_template("contact.html")
from functools import wraps

def add_wrapping_with_style(style):
    def add_wrapping(item):
        @wraps(item) #only overrides item and not all operators like __name__, ...
        def wrapped_item():
            #item is a function so dont forget the item()
            return ('a {} wrapped up box of {}'.format(style, str(item())))
        return wrapped_item
    return add_wrapping


@add_wrapping_with_style('horribly')
@add_wrapping_with_style('beautifully')
##@add_bow //could add another wrapping
def new_gpu():
    return 'a new Tesla p100 GPU'

##print new_gpu.__name__ # -> wrapped_item
print new_gpu()
