from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Section(
                    classs='''block-list''',
                    data = (
                        Header(

                            data = ('''A block list header''',)
                        ), 
                        Ul(

                            data = (
                                Li(

                                    data = (
                                        Div(

                                            data = (
                                                P(
                                                    classs='''list-header''',
                                                    data = (
                                                        Img(
                                                            src='''https://lorempixel.com/30/30/animals''',
                                                            classs='',
                                                            height='',
                                                            width='',
                                                            alt='',
                                                        ), )
                                                ), )
                                        ), )
                                ), 
                                Li(

                                    data = (
                                        Div(

                                            data = (
                                                P(
                                                    classs='''list-header''',
                                                    data = ('''DOUBLE LINE''',)
                                                ), 
                                                P(
                                                    classs='''list-subheader dark''',
                                                    data = ('''Now with an icon''',)
                                                ), )
                                        ), 
                                        Div(

                                            data = (
                                                Img(
                                                    src='''https://lorempixel.com/30/30/animals''',
                                                    classs='',
                                                    height='',
                                                    width='',
                                                    alt='',
                                                ), )
                                        ), )
                                ), 
                                Li(

                                    data = (
                                        Div(

                                            data = (
                                                P(
                                                    classs='''list-header''',
                                                    data = ('''DOUBLE LINE''',)
                                                ), 
                                                P(
                                                    classs='''list-subheader dark''',
                                                    data = ('''What about a two icons??''',)
                                                ), )
                                        ), 
                                        Div(

                                            data = (
                                                Img(
                                                    src='''https://lorempixel.com/30/30/animals''',
                                                    classs='',
                                                    height='',
                                                    width='',
                                                    alt='',
                                                ), 
                                                Img(
                                                    src='''https://lorempixel.com/30/30/animals''',
                                                    classs='',
                                                    height='',
                                                    width='',
                                                    alt='',
                                                ), )
                                        ), )
                                ), 
                                Li(

                                    data = (
                                        P(
                                            classs='''list-header''',
                                            data = ('''IMAGE ON THE RIGHT''',)
                                        ), 
                                        Img(
                                            src='''https://lorempixel.com/30/30/animals''',
                                            classs='',
                                            height='',
                                            width='',
                                            alt='',
                                        ), )
                                ), 
                                Li(
                                    classs='''with-chevron''',
                                    data = (
                                        A(
                                            href='''#''',
                                            data = ('''Independent With a Chevron''',)
                                        ), )
                                ), )
                        ), )
                ), 
                Section(
                    classs='''block-list''',
                    data = (
                        Header(

                            data = ('''Radio buttons list''',)
                        ), 
                        Ul(

                            data = (
                                Li(

                                    data = (
                                        Input(
                                            typee='''radio''',
                                            name='''delicious''',
                                            id='''eggs''',
                                            value='''eggs''',
                                            checked='',
                                        ), 
                                        Label(
                                            forr='''eggs''',
                                            data = ('''Eggs''',)
                                        ), )
                                ), 
                                Li(

                                    data = (
                                        Input(
                                            typee='''radio''',
                                            name='''delicious''',
                                            id='''bacon''',
                                            value='''bacon''',
                                        ), 
                                        Label(
                                            forr='''bacon''',
                                            data = ('''Bacon''',)
                                        ), )
                                ), 
                                Li(

                                    data = (
                                        Input(
                                            typee='''radio''',
                                            name='''delicious''',
                                            id='''toast''',
                                            value='''toast''',
                                        ), 
                                        Label(
                                            forr='''toast''',
                                            data = ('''Toast''',)
                                        ), )
                                ), )
                        ), )
                ), 
                Section(
                    classs='''block-list''',
                    data = (
                        Header(

                            data = ('''Look, I gotta Switch''',)
                        ), 
                        Ul(

                            data = (
                                Li(

                                    data = (
                                        Span(
                                            classs='''list-label''',
                                            data = ('''Switch!''',)
                                        ), 
                                        Div(
                                            classs='''switch''',
                                            data = (
                                                Input(
                                                    classs='''switch-input''',
                                                    id='''exampleSwitch''',
                                                    typee='''checkbox''',
                                                    name='''exampleSwitch''',
                                                ), 
                                                Label(
                                                    classs='''switch-paddle''',
                                                    forr='''exampleSwitch''',
                                                    data = (
                                                        Span(
                                                            classs='''show-for-sr''',
                                                            data = ('''Download Kittens''',)
                                                        ), )
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), 
                Section(
                    classs='''block-list''',
                    data = (
                        Header(

                            data = ('''I Hold Forms''',)
                        ), 
                        Ul(

                            data = (
                                Li(

                                    data = (
                                        Input(
                                            typee='''text''',
                                            placeholder='''User name''',
                                        ), )
                                ), 
                                Li(

                                    data = (
                                        Input(
                                            typee='''password''',
                                            placeholder='''Password''',
                                        ), )
                                ), )
                        ), )
                ), 
                Section(
                    classs='''block-list''',
                    data = (
                        Header(

                            data = ('''I Even Have Selectboxes''',)
                        ), 
                        Ul(

                            data = (
                                Li(
                                    classs='''with-dropdown''',
                                    data = (
                                        Select(
                                            name='',
                                            id='',
                                            data = (
                                                Option(

                                                    data = ('''Now''',)
                                                ), 
                                                Option(

                                                    data = ('''Later''',)
                                                ), 
                                                Option(

                                                    data = ('''Eventually''',)
                                                ), 
                                                Option(

                                                    data = ('''Forever''',)
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)