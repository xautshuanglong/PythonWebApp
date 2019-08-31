from django.shortcuts import render
from django.contrib import messages
import logging

logger = logging.getLogger('django')


def hello(request):
    logger.debug('Debug Test log')
    logger.info('Info Test log')

    messages.add_message(request, messages.INFO, 'Hello world.')

    logger.warning('Waring Test log')
    hello_context = dict()
    hello_context['hello'] = 'Hello World!'
    hello_context['decimal_digits'] = 2
    hello_context['threshold'] = [30.5, 60.5, ]
    hello_context['testValues'] = [0, 1, 10, 29, 30, 31, 35, 60, 61, 65, 99.123, 110, 200, 640]
    return render(request, 'hello.html', hello_context)
