kontantflyter = [0] * 2 + [1000] * 9  # sett inn liste
kalkulasjonsrente = 12 / 100  # sett inn rente

NNV = sum(
    kontantflyt / ((1 + kalkulasjonsrente) ** t)
    for kontantflyt, t in zip(kontantflyter, range(0, len(kontantflyter)))
)

print(f"{NNV=}")
