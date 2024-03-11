investeringskostnad = float(input("Investeringskostnad: "))
levetid = int(input("Levetid: "))
restverdi = float(input("Restverdi: "))
salgspris_per_stykk = float(input("Salgspris: "))
produksjonskostnad_per_stykk = float(input("Produksjonskostnad: "))
solgte_enheter_per_år = int(input("Salg pr. år: "))
kalkulasjonsrente = float(input("Rente(prosent): ")) / 100

inntekt_per_år = (
    salgspris_per_stykk - produksjonskostnad_per_stykk
) * solgte_enheter_per_år
nåverdi_inntekter = sum(
    inntekt_per_år / ((1 + kalkulasjonsrente) ** t) for t in range(1, levetid + 1)
)

nåverdi_restverdi = restverdi / ((1 + kalkulasjonsrente) ** levetid)
nåverdi_investeringskostnad = investeringskostnad
NNV = nåverdi_inntekter + nåverdi_restverdi - nåverdi_investeringskostnad
print(f"{NNV=}")
