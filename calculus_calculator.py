
import panel as pn
from sympy import *

pn.extension()

def integration(expression, a=None, b=None):
    x = Symbol("x")
    if a is None or b is None:
        return integrate(expression, x)
    else:
        return integrate(expression, (x, a, b))

def differentiation(expression):
    x = Symbol("x")
    return diff(expression, x)

def limits(expression, limit_value):
    x = Symbol("x")
    return limit(expression, x, limit_value)

def integration_choice_callback(event):
    integration_type = event.new
    if integration_type == 'Definite Integral':
        input_a.disabled = False
        input_b.disabled = False
    else:
        input_a.disabled = True
        input_b.disabled = True

def calculate_callback(event):
    selected_option = select.value
    user_input = input_expression.valuemodels.AutoField(attributes)

    if selected_option == 'Integration':
        integration_type = integration_choice.value
        if integration_type == 'Definite Integral':
            a = input_a.value
            b = input_b.value
            a_value = eval(a.replace('pi', str(pi)))
            b_value = eval(b.replace('pi', str(pi)))
            result = integration(user_input, a_value, b_value)
        else:
            result = integration(user_input)
    elif selected_option == 'Differentiation':
        result = differentiation(user_input)
    elif selected_option == 'Limits':
        limit_value = input_limit.value
        result = limits(user_input, limit_value)
    else:
        result = "Invalid selection"

    output_text.value = result

# Create widgets with improved labels
select = pn.widgets.Select(options=['Choose One', 'Integration', 'Differentiation', 'Limits'], name="Select Calculation:")
input_expression = pn.widgets.TextInput(value='', name="Enter Expression:")
input_limit = pn.widgets.TextInput(value='', name="Limit Value:")
input_a = pn.widgets.TextInput(value='', disabled=True, name="Lower Limit:")
input_b = pn.widgets.TextInput(value='', disabled=True, name="Upper Limit:")
integration_choice = pn.widgets.RadioButtonGroup(options=['Definite Integral', 'Indefinite Integral'], value='Indefinite Integral', inline=True, name="Integration Type:")
calculate_button = pn.widgets.Button(name='Calculate')
output_text = pn.widgets.StaticText(value='', name="Result:", style={'font-weight': 'bold', 'color': 'blue'})

# Link the callback functions to the button click events
calculate_button.on_click(calculate_callback)
integration_choice.param.watch(integration_choice_callback, 'value')

# Create a Panel layout with improved styling
widget_section = pn.Column(
    pn.Row(select),
    pn.Row(input_expression),
    pn.Row(input_limit),
    pn.Row(integration_choice),
    pn.Row(input_a, input_b),
    pn.Row(calculate_button),
    pn.Row(output_text),
    sizing_mode='stretch_width',
    align='center'
)

# Show the Panel application
widget_section.servable()
