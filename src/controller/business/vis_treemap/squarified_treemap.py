import math

class Squarified_Treemap:
    def __init__(self, root):
        self.root = root
        self.layout = []

    def calculateLayout(self):
        self.layout = []  # Limpa o layout anterior (se houver)
        self._calculateLayoutRecursive(self.root, 0, 0, 1, 1)

    def _calculateLayoutRecursive(self, node, x, y, width, height):
        if node.hasChildren():
            self._squarify(node.children, x, y, width, height)
            for i, child in enumerate(node.children):
                if width > height:
                    new_width = child.totalValue * width / node.totalValue
                    self._calculateLayoutRecursive(child, x, y, new_width, height)
                    x += new_width
                    width -= new_width
                else:
                    new_height = child.totalValue * height / node.totalValue
                    self._calculateLayoutRecursive(child, x, y, width, new_height)
                    y += new_height
                    height -= new_height
        else:
            node.x = x
            node.y = y
            node.width = width
            node.height = height
            self.layout.append(node)

    def _squarify(self, items, x, y, width, height):
        aspect_ratio = self._calculateAspectRatio(items, width, height)
        items.sort(key=lambda item: item.value, reverse=True)

        row = []
        row_total = 0
        worst_ratio = float("inf")

        for item in items:
            row.append(item)
            row_total += item.value
            new_ratio = self._calculateWorstAspectRatio(row, width, height)
            if new_ratio > worst_ratio:
                row.pop()
                row_total -= item.value
                self._layoutRow(row, x, y, width, height, row_total, worst_ratio)
                row = [item]
                row_total = item.value
                worst_ratio = float("inf")
            else:
                worst_ratio = new_ratio

        self._layoutRow(row, x, y, width, height, row_total, worst_ratio)

    def _layoutRow(self, items, x, y, width, height, row_total, worst_ratio):
        if width > height:
            row_height = height * row_total / (width * width)
            new_width = row_total / row_height
            new_height = row_height
        else:
            row_width = width * row_total / (height * height)
            new_width = row_width
            new_height = row_total / row_width

        start_x = x
        start_y = y
        for item in items:
            item.x = (x - start_x) / width
            item.y = (y - start_y) / height
            item.width = item.value / new_width
            item.height = item.value / new_height
            x += item.width

    def _calculateAspectRatio(self, items, width, height):
        total_value = sum(item.value for item in items)
        if total_value == 0:
            return 0

        if width > height:
            row_height = height * total_value / (width * width)
            return width / row_height
        else:
            row_width = width * total_value / (height * height)
            return row_width / height

    def _calculateWorstAspectRatio(self, items, width, height):
        if len(items) == 0:
            return float("inf")

        total_value = sum(item.value for item in items)
        max_value = max(item.value for item in items)

        if width > height:
            row_height = height * total_value / width
            return max(width * width * max_value / (row_height * total_value),
                       row_height * row_height * total_value / (width * max_value))
        else:
            row_width = width * total_value / height
            return max(height * height * max_value / (row_width * total_value),
                       row_width * row_width * total_value / (height * max_value))
