def remove_global_links(graph):
    link_frequency = {}

    for page, links in graph.items():
        for link in links:
            link_frequency[link] = link_frequency.get(link, 0) + 1

    # Any link appearing on more than 50% pages is treated as global
    threshold = len(graph) * 0.5

    cleaned_graph = {}
    for page, links in graph.items():
        cleaned_graph[page] = [
            link for link in links if link_frequency.get(link, 0) < threshold
        ]

    return cleaned_graph
