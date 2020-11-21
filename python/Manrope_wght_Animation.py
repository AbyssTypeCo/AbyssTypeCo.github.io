'''animate individual characters in a variable font'''

fontName = 'Manrope-ExtraLight'
txt = 'Manrope'

# steps between min/max range
steps = 24

# variable font range 
variations = listFontVariations(fontName)
axis = list(variations.keys())[0]
minW = variations[axis]['minValue']
maxW = variations[axis]['maxValue']

# rect height range
minH, maxH = 60, 90

# step for each range
stepR = (1.0  - 0.0)  / (steps - 1) # red channel
stepW = (maxW - minW) / (steps - 1) # variable font
stepH = (maxH - minH) / (steps - 1) # rect height

for i in range((steps * 2) - 2):

    if i < steps:
        R = 0.0  + i * stepR
        W = minW + i * stepW
        H = minH + i * stepH
    else:
        R = 1.0  - ((i % steps) + 1) * stepR
        W = maxW - ((i % steps) + 1) * stepW
        H = maxH - ((i % steps) + 1) * stepH
    
    # print(i, R, W)

    newPage(1200, 800)
    font('LunakhodMikro-Regular')

    fill(0, 0, 0)
    rect(0, 0, width(), height())

    fill(0, 0, R)
    text(f'{R:.3f} / {W:.3f}', (20, height() - 20))
    text(f'{i}', (width() - 20, height() - 20), align='right')

    fill(0)
    text(f'min: {minW}', (20, 20))
    fill(0, 0, 1)
    text(f'max: {maxW}', (width() - 20, 20), align='right')
    fill(R, 0, R)
    text(axis, (width() / 2, 20), align='center')

    w = (width() - 40) / len(txt)

    save()
    translate(20, 50)

    # step for character variation
    stepR_ = (1.0 - 0.0)   / (len(txt))
    stepW_ = (maxW - minW) / (len(txt))
    stepH_ = (maxH - minH) / (len(txt))

    T = FormattedString()
    T.fontSize(180)
    T.font(fontName)

    for j, char in enumerate(txt):

        R_ = R + j * stepR_
        W_ = W + j * stepW_
        H_ = H + j * stepH_

        if R_ > 1.0:   R_ -= 1.0
        if W_ > maxW:  W_ -= (maxW - minW)
        if H_ > maxH:  H_ -= (maxH - minH)

        fill(0, 0, R_)
        rect(0, 0, w, H_)
        fill(1, 1, 0)
        text('%.3f' % R_, (5, 10))
        text('%.3f' % W_, (5, 25))

        T.append(char, fill=(0, 0, R_), fontVariations={axis:W_})

        translate(w * 1.0, 0)

        R_ += stepR_
        W_ += stepW_
        H_ += stepH_

    restore()
    text(T, (width() / 2, height() / 2), align='center')

saveImage('~/Desktop/Manrope{wght}.mp4', imageResolution=144)