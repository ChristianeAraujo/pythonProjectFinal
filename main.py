import matplotlib.pyplot as plt
import geopandas as gpd


def read_shapes(name):
    return gpd.read_file(name)


def plot(base1, base2):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    base1.plot(ax=ax1)
    base2.plot(ax=ax2, color="purple")
    ax1.set_title("Area Programatica 1.0", fontsize=20)
    ax2.set_title("Unidades de Saude Municipais", fontsize=20)
    ax1.set_axis_off()
    ax2.set_axis_off()
    plt.show()


def plot_boundaries(base, border):
    fig, ax = plt.subplots(figsize=(12, 8))
    base.plot(ax=ax, color="purple")
    border.boundary.plot(ax=ax, color="green")
    ax.set_title("hospitais da AP1.0 Clipped", fontsize=20)
    ax.set_axis_off()
    plt.show()


if __name__ == '__main__':
    p = 'data/Unidades_de_Saude_Municipais.shp'
    p2 = 'data/AP1.shp'

    hosp = read_shapes(p)
    ap1 = read_shapes(p2).to_crs(hosp.crs)
    hospitais_clipped = gpd.clip(hosp, ap1)
    plot_boundaries(hospitais_clipped, ap1)

