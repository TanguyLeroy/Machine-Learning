# Fonction de standardisation par trajectoire
def standardize_gesture(df_group):
    df = df_group.copy()
    # Standardisation pour les colonnes 'x', 'y', et 'z' : avec les noms de colonnes sans chevrons
    for axis in ['x', 'y', 'z']:
        df[f'{axis}_std'] = (df[axis] - df[axis].mean()) / df[axis].std()
    return df

# Appliquer la standardisation à chaque trajectoire
df = df.groupby(['subject', 'gesture', 'iter'], group_keys=False).apply(standardize_gesture)
#df = df.groupby(['gesture'], group_keys=False).apply(standardize_gesture)  #par geste uniquement


# Calculer le rang du temps 't' dans chaque groupe
df['t_rank'] = df.groupby(['subject', 'gesture', 'iter'])['t'].rank()

# Afficher les données normalisées d'une trajectoire en 3D
subdf = df.loc[(df['gesture'] == 3) & (df['subject'] == 10) & (df['iter'] == 5)]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(subdf['x_std'], subdf['y_std'], subdf['z_std'], c='r', marker='o')

# Statistiques descriptives
print(df.describe().transpose())

# Sauvegarde CSV
df.to_csv('df.csv', index=False)
