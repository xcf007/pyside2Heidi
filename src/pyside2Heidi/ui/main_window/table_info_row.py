from PySide2.QtWidgets import QCheckBox, QComboBox, QHBoxLayout, QLabel, QTableWidgetItem, QWidget
from database.column import Column
from qthelpers import helper_methods


class TableInfoRow:
	def __init__(self, parent, column):
		"""
		@type parent: DatabaseTableInfo
		@type column: Column
		"""
		self.parent = parent
		self.column = column

	@staticmethod
	def generateDataTypesField(dataType=None):
		"""
		@rtype: QComboBox
		"""
		dataTypes = QComboBox()
		dataTypes.addItems(['TINYINT', 'SMALLINT', 'MEDIUMINT', 'INT', 'BIGINT', 'BIT'])
		dataTypes.insertSeparator(dataTypes.count())
		dataTypes.addItems(['FLOAT', 'DOUBLE', 'DECIMAL'])
		dataTypes.insertSeparator(dataTypes.count())
		dataTypes.addItems(['CHAR', 'VARCHAR', 'TINYTEXT', 'TEXT', 'MEDIUMTEXT', 'LONGTEXT'])
		dataTypes.insertSeparator(dataTypes.count())
		dataTypes.addItems(['BINARY', 'VARBINARY', 'TINYBLOB', 'BLOB', 'MEDIUMBLOB', 'LONGBLOB'])
		dataTypes.insertSeparator(dataTypes.count())
		dataTypes.addItems(['DATE', 'TIME', 'YEAR', 'DATETIME', 'TIMESTAMP'])
		dataTypes.insertSeparator(dataTypes.count())
		dataTypes.addItems(['POINT', 'LINESTRING', 'POLYGON', 'GEOMETRY', 'MULTIPOINT', 'MULTILINESTRING', 'MULTIPOLYGON', 'GEOMETRYCOLLECTION'])
		dataTypes.insertSeparator(dataTypes.count())
		dataTypes.addItems(['ENUM', 'SET'])

		if dataType is not None:
			dataTypes.setCurrentIndex(dataTypes.findText(dataType.upper()))

		return dataTypes

	@staticmethod
	def generateIdField(id=''):
		"""
		@rtype: QTableWidgetItem
		"""
		idField = QTableWidgetItem(str(id))
		idField.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
		idField.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

		return idField

	@staticmethod
	def generateNullCheckboxField(allowsNull=True):
		"""
		@rtype: QCheckBox
		"""
		return TableInfoRow.generateCenteredCheckbox(allowsNull)

	@staticmethod
	def generateCenteredCheckbox(checked=False):
		"""
		@rtype: QCheckBox
		"""
		field = QWidget()
		checkbox = QCheckBox()
		layout = QHBoxLayout(field)
		layout.addWidget(checkbox, 0, Qt.AlignHCenter)
		layout.setMargin(1)
		field.setLayout(layout)
		field.checkbox = checkbox
		checkbox.setChecked(checked)

		return field

	@staticmethod
	def generateCollationsField(server):
		"""
		@rtype: QComboBox
		"""
		collations = server.getCollations()

		field = QComboBox()
		field.addItem('')
		for collation in collations:
			field.addItem(collation['Collation'])

		return field

	@staticmethod
	def generateVirtualityField():
		"""
		@rtype: QComboBox
		"""
		field = QComboBox()
		field.addItems(['', 'VIRTUAL', 'PERSISTENT'])

		return field

	@staticmethod
	def generateNameField(index, name=None):
		"""
		@rtype: QTableWidgetItem
		"""
		if name is None:
			name = "Column %s" % index

		return TableInfoRow.generateTextfield(name)

	@staticmethod
	def generateTextfield(defaultText=None):
		"""
		@rtype: QTableWidgetItem
		"""
		if defaultText is None:
			defaultText = ''

		return QTableWidgetItem(defaultText)

	@staticmethod
	def generateDefaultField(column):
		"""
		@type column: Column
		@rtype: QTableWidgetItem
		"""
		if column.autoIncrement:
			defaultText = 'AUTO_INCREMENT'
		elif column.default is None:
			defaultText = 'No default'
		else:
			defaultText = "'%s'" % column.default

		return TableInfoRow.generateTextfield(defaultText)

	def insertAtEnd(self):
		index = self.parent.rowCount()
		self.insertAt(index)

	def insertAt(self, index):
		parent = self.parent
		column = self.column

		self.idField = TableInfoRow.generateIdField(index)
		self.nameField = TableInfoRow.generateNameField(index, column.name)
		self.dataTypesField = TableInfoRow.generateDataTypesField(column.dataType)
		self.lengthField = TableInfoRow.generateTextfield(column.length)
		self.unsignedField = TableInfoRow.generateCenteredCheckbox(column.unsigned)
		self.nullField = TableInfoRow.generateNullCheckboxField(column.allowsNull)
		self.zerofillField = TableInfoRow.generateCenteredCheckbox(column.zerofill)
		self.defaultField = TableInfoRow.generateDefaultField(column)
		self.collationsField = TableInfoRow.generateCollationsField(self.parent.getMainApplicationWindow().currentDatabase.server)
		self.virtualityField = TableInfoRow.generateVirtualityField()

		parent.insertRow(index)
		parent.setItem(index, 0, self.idField)
		parent.setItem(index, 1, self.nameField)
		parent.setCellWidget(index, 2, self.dataTypesField)
		parent.setItem(index, 3, self.lengthField)
		parent.setCellWidget(index, 4, self.unsignedField)
		parent.setCellWidget(index, 5, self.nullField)
		parent.setCellWidget(index, 6, self.zerofillField)
		parent.setItem(index, 7, self.generateDefaultField(column))
		parent.setCellWidget(index, 9, self.collationsField)
		parent.setCellWidget(index, 11, self.virtualityField)
