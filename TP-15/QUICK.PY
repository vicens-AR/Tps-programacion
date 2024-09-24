import py5

array = [30, 5, 20, 60, 50, 15, 45, 10]
generator = None

def quick_sort(arr, low, high):
    if low < high:
        pi_gen = partition(arr, low, high)
        for step in pi_gen:
            yield step
        yield from quick_sort(arr, low, pi_gen.send(None) - 1)
        yield from quick_sort(arr, pi_gen.send(None) + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        yield arr, (i, j)
    arr[i+1], arr[high] = arr[high], arr[i+1]
    yield arr, (i+1, high)
    return i+1

def setup():
    py5.size(800, 400)
    py5.frame_rate(5)
    start_quick_sort()

def draw():
    global generator
    py5.background(255)
    if generator:
        try:
            array, comparing = next(generator)
        except StopIteration:
            generator = None
            comparing = (None, None)
    draw_bars(array, comparing)

def draw_bars(arr, comparing=(None, None)):
    bar_width = py5.width / len(arr)
    for i, value in enumerate(arr):
        if i in comparing:
            py5.fill(255, 0, 0)
        else:
            py5.fill(100, 150, 200)
        py5.rect(i * bar_width, py5.height - value, bar_width, value)

def start_quick_sort():
    global generator
    generator = quick_sort(array[:], 0, len(array) - 1)

py5.run_sketch()
