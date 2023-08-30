from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''polls''',
                    data = (
                        H5(
                            classs='''polls-question''',
                            data = (
                                Span(
                                    classs='''polls-question-label''',
                                    data = ('''Q:''',)
                                ), )
                        ), 
                        Div(
                            classs='''polls-options''',
                            data = (
                                Div(

                                    data = (
                                        Input(
                                            typee='''radio''',
                                            name='''programming''',
                                            value='''Javascript''',
                                            id='''programmingJavascript''',
                                            required='',
                                        ), 
                                        Label(
                                            forr='''programmingJavascript''',
                                            data = ('''Javascript''',)
                                        ), )
                                ), 
                                Div(

                                    data = (
                                        Input(
                                            typee='''radio''',
                                            name='''programming''',
                                            value='''Ruby''',
                                            id='''programmingRuby''',
                                            required='',
                                        ), 
                                        Label(
                                            forr='''programmingRuby''',
                                            data = ('''Ruby''',)
                                        ), )
                                ), 
                                Div(

                                    data = (
                                        Input(
                                            typee='''radio''',
                                            name='''programming''',
                                            value='''Php''',
                                            id='''programmingPhp''',
                                            required='',
                                        ), 
                                        Label(
                                            forr='''programmingPhp''',
                                            data = ('''Php''',)
                                        ), )
                                ), 
                                Div(

                                    data = (
                                        Input(
                                            typee='''radio''',
                                            name='''programming''',
                                            value='''Python''',
                                            id='''programmingPython''',
                                            required='',
                                        ), 
                                        Label(
                                            forr='''programmingPython''',
                                            data = ('''Python''',)
                                        ), )
                                ), )
                        ), 
                        Div(
                            classs='''polls-submit''',
                            data = (
                                Input(
                                    typee='''submit''',
                                    classs='''button''',
                                    value='''Submit Vote''',
                                ), )
                        ), )
                ), 
                Div(
                    classs='''polls''',
                    data = (
                        H5(
                            classs='''polls-question''',
                            data = (
                                Span(
                                    classs='''polls-question-label''',
                                    data = ('''Q:''',)
                                ), )
                        ), 
                        Div(
                            classs='''polls-options''',
                            data = (
                                Div(

                                    data = (
                                        Input(
                                            id='''checkbox1''',
                                            typee='''checkbox''',
                                        ), 
                                        Label(
                                            forr='''checkbox1''',
                                            data = ('''Angular.js''',)
                                        ), )
                                ), 
                                Div(

                                    data = (
                                        Input(
                                            id='''checkbox2''',
                                            typee='''checkbox''',
                                        ), 
                                        Label(
                                            forr='''checkbox2''',
                                            data = ('''React.js''',)
                                        ), )
                                ), 
                                Div(

                                    data = (
                                        Input(
                                            id='''checkbox3''',
                                            typee='''checkbox''',
                                        ), 
                                        Label(
                                            forr='''checkbox3''',
                                            data = ('''Vue.js''',)
                                        ), )
                                ), 
                                Div(

                                    data = (
                                        Input(
                                            id='''checkbox4''',
                                            typee='''checkbox''',
                                        ), 
                                        Label(
                                            forr='''checkbox4''',
                                            data = ('''Knockout.js''',)
                                        ), )
                                ), )
                        ), 
                        Div(
                            classs='''polls-submit''',
                            data = (
                                Input(
                                    typee='''submit''',
                                    classs='''button''',
                                    value='''Submit Vote''',
                                ), )
                        ), )
                ), )
        ), )
)