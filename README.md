# Venezuela - Estados, Municipios y Parroquias

[![Odoo Version](https://img.shields.io/badge/Odoo-14.0--18.0%2B-714B67?style=flat&logo=odoo)](https://www.odoo.com)
[![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0.html)
[![Country](https://img.shields.io/badge/Country-Venezuela%20%F0%9F%87%BB%F0%9F%87%AE-00247D)](https://ine.gob.ve)

Módulo personalizado para **Odoo** que incorpora la estructura político-territorial completa y oficial de la **República Bolivariana de Venezuela** dentro del modelo de **Contactos (`res.partner`)**.

Permite la selección jerárquica en cascada (**Estado → Municipio → Parroquia**) con datos totalmente precargados al momento de instalar el módulo, adaptado tanto para **Personas (Físicas)** como para **Empresas (Compañías)**.

---

## 🚀 Características Principales

* **📦 Datos Precargados al 100%:**
  * **24 Entidades Federales** (23 Estados + Distrito Capital y Dependencias Federales).
  * **+335 Municipios** vinculados a sus respectivos estados.
  * **+1,100 Parroquias** (urbanas y rurales) vinculadas a sus municipios.
* **🔄 Filtro Dinámico en Cascada:**
  * Al seleccionar **Venezuela** como país, el campo *Estado* despliega los estados del país.
  * Al seleccionar un *Estado*, el campo *Municipio* se filtra automáticamente mostrando únicamente los municipios pertenecientes a dicho estado.
  * Al seleccionar un *Municipio*, el campo *Parroquia* restringe sus opciones únicamente a las parroquias pertenecientes a ese municipio.
* **👥 Soporte Integral en Contactos (`res.partner`):**
  * Compatible con fichas individuales de **Personas**, **Empresas**, direcciones de **Facturación** y direcciones de **Entrega/Despacho**.
* **🖨️ Formateo de Dirección Física:**
  * Integración con la representación impresa de direcciones para reportes, presupuestos, guías de despacho y facturas fiscalmente adaptadas a Venezuela (SENIAT).
* **🔍 Búsqueda Rápida y Autocompletado:**
  * Los campos permiten la búsqueda incremental por teclado (autocomplete) para agilizar el registro de datos.

---


## 💡 Modo de Uso

1. Vaya al módulo de **Contactos** (`res.partner`).
2. Cree un nuevo contacto o edite uno existente (Persona o Empresa).
3. Seleccione **Venezuela** en el campo **País**.
4. Seleccione el **Estado** deseado.
5. Verifique cómo el campo **Municipio** se actualiza para mostrar únicamente las opciones del estado seleccionado.
6. Seleccione el **Municipio** y observe cómo el campo **Parroquia** filtra las parroquias asociadas.
7. Complete la dirección física (Calle, Edificio/Casa, Punto de referencia) y guarde.

---

## 🔧 Especificaciones Técnicas

* **Dependencias:**
  * `base`
  * `contacts`
* **Modelos Creados / Extendidos:**
  * `res.country.state` *(Extendido)*
  * `res.country.state.municipality` *(Nuevo)*
  * `res.country.state.parish` *(Nuevo)*
  * `res.partner` *(Extendido)*
* **Compatibilidad de Ediciones:**
  * Odoo Community Edition
  * Odoo Enterprise Edition
  * Odoo.sh / On-Premise / Docker

---

## 🤝 Contribuciones

Las contribuciones, reportes de errores (*issues*) y sugerencias son bienvenidas.

---

## 📄 Licencia

Este proyecto está bajo la Licencia **LGPL-3** (GNU Lesser General Public License v3.0). Consulte el archivo `LICENSE` para más información.
