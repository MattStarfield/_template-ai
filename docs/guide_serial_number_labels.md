# Guide: Serial Number Labels

## Serial Number Format
Product Serial Numbers (or Unique Identifiers) can be in any format that suits the product needs, as long as they uniquely identify a specific unit of the production series. However, the format chosen for Serial Numbers can provide some additional benefits beyond uniquely identifying units in a series, such as:

* Production Time-stamp
* Grouping Production Batches or Lots
* Concise (Minimal Number of Characters)
* Consistent (Fixed Number of Characters)
* Easily Human Readable
* Easily Generate New Batch of SNs

To this end, I suggest the following Serial Number Format:

**AABB.CCC** _(e.g. 2139.001)_, where:
* **AA**  = 2-digit **YEAR**
* **BB**  = 2-digit **WEEK NUMBER**
* **CCC** = 3-digit **SEQUENTIAL ID**

With this format, a manufacturer can support unique serial numbers for up to 1,000 units per week.<br>

Each Serial Number automatically includes a "Time-stamped" **Batch Number** (**AABB**) that indicates the week and year it was produced, as well as associating all of the other units that were produced in that "batch", which can be helpful for tracking and identifying production errors.

## Selecting Serial Number Labels
While Serial Numbers can be stuck onto a product with any old adhesive label, one should carefully consider the type of label material selected. Many products will experience extreme conditions during the production process or during operation, such as exposure to:

* extreme temperature fluctuations
* moisture / humidity
* sweat, oils, chemical solvents
* UV radiation (e.g. direct sunlight)

Most standard "office quality" labels (e.g. mailing labels, label-makers) will not stand up to these conditions. Their ink may fade or run, the paper could dissolve or tear, the adhesive may fail, or worse yet flow into a area that may affect the device's operation. For these reasons, it's important to select an appropriate label for this use case.

On the other side of the label spectrum, there are labels that are designed specifically for use on products and PCBs that will be exposed to the harsh conditions mentioned above (e.g. [Brady Circuit Board Labels](https://www.bradyid.com/labels/circuit-board)). These labels are an excellent choice for Serial Number Labels, however they typically require an expensive specialty printer, or to be pre-ordered from a company that will provide custom-printed labels. In many cases, these options are not time or cost effective.

To achieve the durability we require from our labels with the convenience of on-demand printing from any standard laser printer, I have had great success with

[**OnlineLabels.com OL5400LP - Weatherproof Polyester Laser - 1" x 0.375" Small Rectangle Labels**<br><br><img src="/img/assets/ol5400lp.png" alt="ol5400lp.png" width="600">](https://www.onlinelabels.com/products/OL5400LP?search=OL5400LP&st=s)

* Weatherproof materials
* Strong Self-Adhesive
* Laser Printer compatible
* 8.5" x 11" Sheets of 154 labels each
* Small Size: 1" x 0.375"

## Generating Serial Number Labels
OnlineLabels.com also provides an online label layout tool called [Maestro Label Designer](https://maestro.onlinelabels.com/designer/maestro.aspx#). The _Maestro Label Designer_ tool allows you to import a `.csv` list of Serial Numbers and format them to the positions of the labels on the sheet for printing. You can even generate scannable barcode labels of your Serial Numbers!

One drawback of _Maestro Label Designer_ is that it requires an _Activation Code_ for full access. OnlineLabels.com provides a free activation code when you purchase their labels, but it expires after some time. Fortunately, the only drawback (so far) of an expired activation is that the first 22 labels (on our 154 label sheet) have a watermark on them. So, if we're willing to sacrifice 22 labels from every sheet, we can continue using _Maestro Label Designer_ indefinitely!

Here are the steps for creating Serial Number Labels with _Maestro Label Designer_ using the [Serial Number Format](#serial-number-format) described above:

1. Open a spreadsheet file

1. Enter the **Batch Number** in cell A1 (e.g. B2139)

1. Enter the 1st Serial Number in cell A2 (e.g. B2139.001)

1. Skip cells A3 to A22. These will be the watermarked "waste" labels

1. Re-enter the 1st Serial Number in cell A23 (e.g. B2139.001)

1. Enter the 2nd Serial Number in cell A24 (e.g. B2139.002)

1. Highlight both cells A23 and A24 and fill-down to generate as many Serial Numbers as you'll need for the Batch<br><img src="/img/assets/serial_number_spreadsheet.png" alt=".jpg" width="150">

1. Export the Serial Number List as a `.csv` file

1. Open [Maestro Label Designer](https://maestro.onlinelabels.com/designer/maestro.aspx#)
      * Log-in or Create a User Account

1. Click **Design New Label > Blank Tamplates**<br><img src="/img/assets/maestro_design_new_label.png" alt="maestro_design_new_label.png" width="200">

1. Search "**OL5400**" and Click on the OL5400 result<br><img src="/img/assets/maestro_ol5400.png" alt="maestro_ol5400.png" width="300">

1. Click **Tools > Mail Merge**, then **Start Mail Merge**<br><img src="/img/assets/maestro_mail_merge.png" alt="maestro_mail_merge.png" width="300"> <img src="/img/assets/maestro_start_mail_merge.png" alt="maestro_start_mail_merge.png" width="300">

1. Click **Add a new mail merge list**, then **Next Step**<br><img src="/img/assets/maestro_add_new_mail_merge.png" alt="maestro_add_new_mail_merge.png" width="400">

1. Import your `.csv` file

1. Choose **Simple Text Field**, Select the **Batch Number**, Click **>** to add the field to the label, then Click **Add To Design**<br><img src="/img/assets/maestro_add_fields.png" alt="maestro_add_fields.png" width="400">

1. Click the **Text Field** to select it<br><img src="/img/assets/maestro_text_field.png" alt="maestro_text_field.png" width="400">

1. Click **Align > Center Middle** to center the text field on the label<br><img src="/img/assets/maestro_align.png" alt="maestro_align.png" width="400">

1. Click and drag the boarders of the text box until they are at the edge of the label border<br><img src="/img/assets/maestro_stretch.png" alt="maestro_stretch.png" width="400">

1. In the Left Sidebar, Click **Align > Center** to center-justify the test,<br>then **Increase the Font Size** until the sample text fills the inner dotted border of the label<br><img src="/img/assets/maestro_size.png" alt="maestro_size.png" width="400">

1. Click **Preview** to see an example Serial Number<br>
Continure adjusting the **Font Size** and **Position** until the text slightly overflows the center dotted border of the label <br><img src="/img/assets/maestro_preview.png" alt="maestro_preview.png" width="500">

1. Click **Quick Save**, then name the design after the **Batch Number** and Click **Save Design**<br><img src="/img/assets/maestro_save.png" alt="maestro_save.png" width="400">

1. Click **Print Labels**, then Click **Print Now**<br><img src="/img/assets/maestro_print.png" alt="maestro_print.png" width="200">

1. On the **Activation Warning**, Click **or continue printing with watermark**<br><img src="/img/assets/maestro_print_with_watermark.png" alt="maestro_print_with_watermark.png" width="400">

1. Click **Print Entire File**, then Click **Print**<br><img src="/img/assets/maestro_print_entire_file.png" alt="maestro_print_entire_file.png" width="400">

1. Click **Download and Print**<br><img src="/img/assets/maestro_download_and_print.png" alt="maestro_download_and_print.png" width="400">

1. Maestro will now generate a PDF with the serial numbers spaced for the OL5400LP labels. You can see the first several rows are obscured with the Activation Warning, but our usable Serial Number Labels start below the warning message<br><img src="/img/assets/maestro_pdf.png" alt="maestro_pdf.png" width="400">

1. Load the label sheets into a Laser Printer and print the PDF dircectly onto the label sheet<br>**NOTE: Be sure the printer settings do not alter the position or scaling of the file**<br><img src="/img/assets/maestro_print_settings.png" alt="maestro_print_settings.png" width="600">
