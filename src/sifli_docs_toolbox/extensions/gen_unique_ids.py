from sphinx.transforms import SphinxTransform
from typing import Any
from docutils import nodes

class unique_ids(SphinxTransform):
    """
    Suffix IDs/anchors to make them unique, e.g.
    {overview, features, ..., overview} ->
    {overview, features, ..., overview-1}
    """
    default_priority = 500
    used_ids = set()

    def apply(self, **kwargs: Any) -> None:
        # if (self.app.builder.name != "singlehtml") and (self.app.builder.name != "simplepdf"):
        #     return

        def make_unique_id(node, id_):
            """
            A node contains multiple ids, the first is the title
            text converted to ID, then, if present, the label
            e.g.:
              .. _documentation+a label:

              My header
              ---------

            becomes:
              ["my-header", "documentation-a-label"]

            The first is the one is the one we worry about collision
            """
            counter = 1
            id__ = id_
            while id__ in self.used_ids:
                id__ = f"{id_}-{counter}"
                counter += 1
            self.used_ids.add(id__)
            node['ids'][0] = id__

        # findall (Docutils >= 0.18.1) returns an iterator,
        # and deprecates traverse (returns a list).
        # Sphinx 7.1.2 requires Docutils >= 0.18.1
        for node in self.document.findall():
            if (not isinstance(node, nodes.Text) and
                'ids' in node and node['ids']):
                make_unique_id(node, node['ids'][0])


def setup(app):
    app.add_transform(unique_ids)
    
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }