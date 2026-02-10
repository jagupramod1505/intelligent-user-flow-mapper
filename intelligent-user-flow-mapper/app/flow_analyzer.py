from noise_filter import remove_global_links

def build_user_flow(raw_graph):
    clean_graph = remove_global_links(raw_graph)

    nodes = []
    edges = []

    for page, links in clean_graph.items():
        nodes.append({"id": page, "label": page.split("/")[-1] or "Home"})

        for link in links:
            edges.append({"source": page, "target": link})

    return {
        "nodes": nodes,
        "edges": edges
    }
