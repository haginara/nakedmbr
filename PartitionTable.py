#!/usr/bin/python
"""
    size of partition table is 16bytes
"""

import os
import sys
from struct import *
from partition_table import *

__author__ = "Jonghak Choi"

__license__ = "GPL"
__email__ = "haginara@gmail.com"


class PartitionTable:
	def __init__(self):
		bootable_flag			= ''
		starting_chs_address	= 0
		partition_type			= ''
		ending_chs_address		= 0
		starting_lba_address	= 0
		size_in_sector			= 0 
		
	def setPartitionTable(self, pTable):
		self.bootable_flag			= BOOTABLE_FLAG[int(pTable[0], 16)]
		self.starting_chs_address	= int(''.join(pTable[1:3]), 16)
		self.partition_type			= PARTITION_TYPE[int(pTable[4], 16)]
		self.ending_chs_address		= int(''.join(pTable[5:7]), 16)
		self.starting_lba_address	= int(''.join(pTable[8:11])[::-1], 16)
		self.size_in_sector			= int(''.join(pTable[12:15])[::-1], 16)

	def calcCHS(chs):
		head	= chs >> 16
		sector	= (chs << 10) >> 8
		cylnder	= ( (chs << 8) ^ 49152 ) + (chs << 16) 

	def calcSizeByCHS(self):
		start_chs	= hex(starting_chs_address)
		end_chs		= hex(ending_chs_address)
	
	def getSizeLBA(self):
		return self.size_in_sector * SECTOR_SIZE
	
	def getBootableFlag(self):
		return self.bootable_flag

	def getPartitionType(self):
		return self.partition_type
	
	def getStartingLBAAddress(self):
		return self.starting_chs_address
		

def main():
	drive = sys.argv[1]
	drive = file('/dev/'+ drive)
	mbr = drive.read(512)
	char =[]

	for character in mbr:
		char.append( hex(ord(character))[2:] )

	grub = mbr[0x180:0x184]
	print grub

	NT_Drive_Serial_Number = char[0x1b8:0x1bc][::-1]
	NT_Drive_Serial_Number = ''.join(NT_Drive_Serial_Number).upper()
	print "[*] NT DRIVER SERIAL NUMBER : " + NT_Drive_Serial_Number
	print ''

	

	executable_code = char[0:138]
	print "[*] Executable Code"
	#print ''.join(executable_code)

	partition_table = []
	start = START_PARTITION_TABLE
	for i in range(4):
		partition_table.append( char[start: start + PARTITION_TABLE_LENGTH ] )
		start = start + PARTITION_TABLE_LENGTH
		#print partition_table[i]

	drive.close()
	pt = PartitionTable()
	for i in range(4):
		pt.setPartitionTable(partition_table[i])
		print "[*] Partition Table:", i
		print "[*] Bootable Flag : " + pt.getBootableFlag()
		print "[*] Partition Type: " + pt.getPartitionType()
		print "[*] Starting Relative Address : " , pt.getStartingLBAAddress()
		print "[*] Partition Size: " , pt.getSizeLBA()/pow(1024,2) , "MByte"
		print ''


if __name__ == '__main__':
	main()
