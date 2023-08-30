from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Nav(
                    classs='''top-bar topbar-responsive''',
                    data = (
                        Div(
                            classs='''top-bar-title''',
                            data = (
                                Span(
                                    data_responsive_toggle='''topbar-responsive''',
                                    data_hide_for='''medium''',
                                    data = (
                                        Button(
                                            classs='''menu-icon''',
                                            typee='''button''',
                                            data_toggle='',
                                        ), )
                                ), 
                                A(
                                    classs='''topbar-responsive-logo''',
                                    href='''#''',
                                    data = (
                                        Strong(

                                            data = ('''Site Title''',)
                                        ), )
                                ), )
                        ), 
                        Div(
                            id='''topbar-responsive''',
                            classs='''topbar-responsive-links''',
                            data = (
                                Div(
                                    classs='''top-bar-right''',
                                    data = (
                                        Ul(
                                            classs='''menu simple vertical medium-horizontal''',
                                            data = (
                                                Li(

                                                    data = (
                                                        A(
                                                            href='''#''',
                                                            data = ('''Home''',)
                                                        ), )
                                                ), 
                                                Li(

                                                    data = (
                                                        A(
                                                            href='''#''',
                                                            data = ('''About''',)
                                                        ), )
                                                ), 
                                                Li(

                                                    data = (
                                                        A(
                                                            href='''#''',
                                                            data = ('''Services''',)
                                                        ), )
                                                ), 
                                                Li(

                                                    data = (
                                                        A(
                                                            href='''#''',
                                                            data = ('''Works''',)
                                                        ), )
                                                ), 
                                                Li(

                                                    data = (
                                                        A(
                                                            href='''#''',
                                                            data = ('''News''',)
                                                        ), )
                                                ), 
                                                Li(

                                                    data = (
                                                        A(
                                                            href='''#''',
                                                            data = ('''Contact''',)
                                                        ), )
                                                ), 
                                                Li(

                                                    data = (
                                                        Button(
                                                            typee='''button''',
                                                            classs='''button hollow topbar-responsive-button''',
                                                            data = ('''Categories''',)
                                                        ), )
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)