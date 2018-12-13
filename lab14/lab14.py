#!/usr/bin/env python

import sys
import numpy as np
import scanpy.api as sc
import matplotlib
matplotlib.use("Agg")
sc.settings.autoshow = False

#Unfiltered
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
adata.var_names_make_unique()
#sc.tl.pca(adata, n_comps=50, zero_center=True, svd_solver='auto', random_state=0, return_info=False, dtype='float32', copy=False, chunked=False, chunk_size=None)
#sc.pl.pca(adata, save='unfiltered.png')

sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=True)
#sc.tl.pca(adata, n_comps=50, zero_center=True, svd_solver='auto', random_state=0, return_info=False, dtype='float32', copy=False, chunked=False, chunk_size=None)
#sc.pl.pca(adata, save="filtered")
#scanpy.api.pp.filter_cells(data, min_counts=None, min_genes=None, max_counts=None, max_genes=None, copy=False)
sc.pp.neighbors(adata, n_neighbors=15)
sc.tl.louvain(adata, resolution=None)
#sc.tl.tsne(adata,n_pcs=None, use_rep=None, perplexity=30, early_exaggeration=12, learning_rate=1000, random_state=0, use_fast_tsne=True, n_jobs=None, copy=False)
#sc.pl.tsne(adata, color = "Dbi", save = ("Dbi_gene"))

sc.tl.umap(adata, min_dist=0.5, spread=1.0, n_components=2, maxiter=None, alpha=1.0, gamma=1.0, negative_sample_rate=5, init_pos='spectral', random_state=0, a=None, b=None, copy=False)
sc.pl.umap(adata, color = "Cdc42", save = ("Cdc42_gene"))

#sc.tl.rank_genes_groups(adata, groupby="louvain", method='t-test_overestim_var', corr_method='benjamini-hochberg')
#sc.pl.rank_genes_groups(adata, groupby="louvain", color="louvain", save="t_test")

#sc.tl.rank_genes_groups(adata, groupby="louvain", method='logreg')
#sc.pl.rank_genes_groups(adata, color="louvain", save="logreg")