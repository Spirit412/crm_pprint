from sqlalchemy import MetaData
from graphviz import Digraph

# в ппке core файл base куда импортированы все модели и Base из файла db
from core import base
from sqlalchemy_schemadisplay import create_uml_graph, _render_table_html, show_schema_graph, show_uml_graph, \
    create_schema_graph
from sqlalchemy.orm import class_mapper

#  http://magjac.com/graphviz-visual-editor/
# lets find all the mappers in our model
def write_uml():
    # lets find all the mappers in our model
    mappers = []
    for attr in dir(base):
        if attr[0] == '_': continue
        try:
            cls = getattr(base, attr)
            mappers.append(class_mapper(cls))
        except:
            pass

    graph_out1 = create_uml_graph(mappers,
                                  show_operations=False,  # not necessary in this case
                                  show_multiplicity_one=True,  # some people like to see the ones, some don't
                                  show_attributes=True,
                                  show_inherited=True,
                                  )
    with open('schema_uml.txt', 'w', encoding='utf-8') as f:
        f.write(str(graph_out1))

    graph_out = create_schema_graph(metadata=MetaData("postgresql://postgres:postgres@localhost:6532/fastapi"),
                                    show_datatypes=False,  # can get large with datatypes
                                    show_indexes=False,  # ditto for indexes
                                    rankdir='LR',  # From left to right (LR), top to bottom (TB)
                                    concentrate=True,  # Don't try to join the relation lines together,
                                    )
    with open('schema_schema.txt', 'w', encoding='utf-8') as f:
        f.write(str(graph_out))

write_uml()
