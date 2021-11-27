def bilinear_interpolation(img, size):
    src_height, src_width, channels = img.shape
    dst_height, dst_width = size[0], size[1]
    print("src_height: ", src_height, "src_width: ", src_width)
    print("dst_height: ", dst_height, "dst_width: ", dst_width)
    dst_img = np.zeros((dst_height, dst_width, 3), dtype=np.uint8)
    for i in range(3):
        for j in range(dst_width):
            for k in range(dst_height):
                src_x = (j + 0.5) * float((src_width / dst_width)) - 0.5
                src_y = (k + 0.5) * float((src_height / dst_height)) - 0.5

                src_x0 = int(np.floor(src_x))
                src_x1 = min(int(np.ceil(src_x)), src_width - 1)
                src_y0 = int(np.floor(src_y))
                src_y1 = min(int(np.ceil(src_y)), src_height - 1)

                dst_img[j, k, i] = int(
                    (src_x1 - src_x) * (src_y1 - src_y) * img[src_x0, src_y0, i] + (src_x1 - src_x) * (src_y - src_y0) *
                    img[src_x0, src_y1, i] + (src_x - src_x0) * (src_y1 - src_y) * img[src_x1, src_y0, i] + (
                                src_x - src_x0) * (src_y - src_y0) * img[src_x1, src_y1, i])

    return dst_img


img = cv.imread("lenna.png")
dst = bilinear_interpolation(img, [1000, 1000])
cv.imshow("bint", dst)
cv.waitKey(0)