import os

import matplotlib.pyplot as plt
import geopandas as gpd


def read_shapes(name):
    return gpd.read_file(name)


def plot_boundaries(base, border, name='Hospitais da AP1.0'):
    fig, ax = plt.subplots(figsize=(12, 8))
    base.plot(ax=ax, color="purple")
    border.boundary.plot(ax=ax, color="green")
    ax.set_title(name, fontsize=20)
    ax.set_axis_off()
    plt.savefig(f'output/{name}.png')
    plt.show()


def convert_crs(origin, destination):
    # Recebe arquivos do tipo GEOPANDAS, utiliza a informação de CRS e compatibiliza os CRS entre os arquivos.
    return destination.to_crs(origin.crs)


def main(path):
    # Three examples of list comprehension
    #
    files = [f for f in os.listdir(path) if f.endswith('shp')]
    aps = [read_shapes(os.path.join(path, ap)) for ap in files if ap.startswith('A')]
    hospitais = read_shapes(os.path.join(path, 'Unidades_de_Saude_Municipais.shp'))
    aps = [convert_crs(hospitais, ap) for ap in aps]
    clipped = [gpd.clip(hospitais, ap) for ap in aps]

    for i in range(len(clipped)):
        plot_boundaries(clipped[i], aps[i], f'Hospitais da {aps[i].COD_AP_SMS.loc[0]}')
    return clipped, aps


if __name__ == '__main__':
    # p = 'data/Unidades_de_Saude_Municipais.shp'
    # p2 = 'data/AP1.shp'
    #
    # hosp = read_shapes(p)
    # ap1 = read_shapes(p2).to_crs(hosp.crs)
    # hospitais_clipped = gpd.clip(hosp, ap1)
    # plot_boundaries(hospitais_clipped, ap1)

    p3 = 'data'
    clips, rs = main(p3)

