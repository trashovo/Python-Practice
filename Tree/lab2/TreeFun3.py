"""Ученые изучают поведение птиц, вьющих гнезда на бинарном дереве, и хотят
разместить в его узлах камеры. Каждая камера может обозревать узел, в котором она
расположена, а также непосредственного предка и непосредственных потомков этого узла. По
заданному бинарному дереву требуется определить, какое минимальное количество камер
потребуется ученым для того, чтобы полностью покрыть наблюдением все узлы дерева."""

from Class2 import *


def main():
    print("Введите числа:")
    while True:
        try:
            nums = list(map(int, input().split()))
            if len(nums) == 0:
                print("Введите хотя бы одно число")
                continue
            break
        except ValueError:
            print("Неверное значение")

    root = None
    for x in nums:
        if root is None:
            root = Node(x)
        else:
            root.insert(x)


    print("Дерево")
    root.levelorder()

    camera = CameraSystem()
    camera.solve(root)

    print(f"Минимальное количество камер: {camera.cameras}")

    positions_str = ", ".join(str(x) for x in camera.camera_positions)
    print(f"Камеры установлены в узлах: {positions_str}")


if __name__ == "__main__":
    main()