DATA_TEST = "target area: x=20..30, y=-10..-5"
DATA = "target area: x=235..259, y=-118..-62"


def run(x_range, y_range):
    results = 0

    #    xv, yv = 17, -4
    max_y = 0
    max_v = None

    for xv_start in range(-200, 200):
        for yv_start in range(-200, 200):
            xv, yv = xv_start, yv_start
            step = 0
            ys = [0]
            x, y = 0, 0
            # print(f"Starting with v({xv}, {yv})")

            while True:
                x += xv
                y += yv
                ys.append(y)

                if xv > 0:
                    xv -= 1
                elif xv < 0:
                    xv += 1
                yv = yv - 1

                step += 1
                # print(f"step {step}: ({x}, {y}) v({xv}, {yv})")
                if x_range[0] <= x <= x_range[1] and y_range[0] <= y <= y_range[1]:
                    print(f"Hit target on step {step} at ({x}, {y})")
                    max_y = max(max_y, max(ys))
                    max_v = (xv, yv)
                    break
                if x > x_range[1] or y < y_range[0]:
                    #        print(f"Missed after step {step}")
                    break
                if step > 1000:
                    print("Too many steps")
                    break

    results = max_y
    print(max_v)
    return results


if __name__ == "__main__":
    data = DATA
    x_range, y_range = data.replace("target area: ", "").split(",")
    x_range = [int(x) for x in x_range.replace("x=", "").split("..")]
    y_range = [int(y) for y in y_range.replace("y=", "").split("..")]
    print(f"Target: ({x_range}, {y_range})")
    results = run(x_range, y_range)
    print(results)


# 6903 is correct
