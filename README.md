# fx-settlement-ledger

## Français

Séparer change et arrondi dans un règlement multidevise déclaré.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m fx_settlement_ledger examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Produit un reçu arithmétique de règlement partiel avec sens de cotation explicite, taux fournis, frais et ligne d’arrondi séparée. Les écritures signées débit−crédit s’équilibrent exactement.

### Limites

Contrat de calcul illustratif, sans taux de marché, règle fiscale ou recommandation comptable. Demi-pair et nombre de décimales déclarés ; devise différente obligatoire, remboursements et surpaiements hors périmètre.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Separate exchange effects and rounding in declared FX settlement.

Synthetic data; no network access or secret required.

```sh
python -m fx_settlement_ledger examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Produces an arithmetic partial-settlement receipt with explicit quote direction, supplied rates, fees and separate rounding line. Signed debit−credit entries balance exactly.

### Limits

Illustrative calculation contract, no market rates, tax rule or accounting recommendation. Declared half-even rounding and minor digits; distinct currencies required, refunds and overpayments unsupported.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Separar cambio y redondeo en una liquidación multidivisa declarada.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m fx_settlement_ledger examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Produce recibo aritmético de liquidación parcial con sentido de cotización explícito, tasas suministradas, comisiones y redondeo separado. Asientos débito−crédito equilibran exactamente.

### Límites

Contrato ilustrativo, sin tipos de mercado, normas fiscales o recomendación contable. Redondeo al par y decimales declarados; divisas distintas obligatorias, sin devoluciones o sobrepagos.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://docs.python.org/3/library/decimal.html
