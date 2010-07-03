#!/usr/bin/python

import os
import sys

__author__ = 'Jonghak Choi'
__license__ = 'GPL'
__contact__ = 'haginara@gmail.com'

SECTOR_SIZE = 512
NUMBER_OF_PARTITION_TABLE = 4
START_PARTITION_TABLE = 446
PARTITION_TABLE_LENGTH = 16
MAGIC_NUMBER = 0x55AA

BootableFlag = [
    ('BOOTING_ENABLE', 0x80),
    ('BOOTING_UNENABLE', 0x0)]
   
BOOTABLE_FLAG = dict(BootableFlag+[(e[1], e[0]) for e in BootableFlag])

STARTING_CHS_ADDRESSS = 0x000000

PartitionType = [
    ('Empty',                                     0x00),
    ('FAT12_PRIMARY_CHS',                         0x01),
    ('FAT16_CHS',                                 0x05),
    ('Microsoft_Extended_Partiton_CHS',            0x05),
    ('BIGDOS_FAT16_CHS',                        0x06),
    ('NTFS',                                    0x07),
    ('FAT32_CHS',                                0x0B),
    ('FAT32_USING_BIOS_INT13h_LBA',                0x0C),
    ('BIGDOS_FAT16_USING_BIOS_INT13h_LBA',        0x0E),
    ('Extended_Partition_USING_BIOS INT13h_LBA',0x0F),
    ('Hidden_FAT12_CHS',                        0x11),
    ('Hidden_FAT16_16MB_TO_32MB_CHS',            0x14),
    ('Hidden_FAT16_32MB_TO_2GB_CHS',            0x16),
    ('Hidden_FAT32_CHS',0x1B),
    ('Hidden_FAT32_LBA',0x1C),
    ('Hidden_FAT16_32MB_TO_2GB_LBA',0x1E),
    ('MICROSOFT_MBR_DYNAMIC_DISK',0x42),
    ('SOLARIS_x86_OR_LINUX_SWAP',0x82),
    ('LINUX',0x83),
    ('HIBERNATION',0x84),
    ('LINUX_EXTENDED',0x85),
    ('NTFS_VOLUME_SET',0x86),
    ('NTFS_VOLUME_SET',0x87),
    ('HIBERNATION',0xA0),
    ('HIBERNATION',0xA1),
    ('FreeBSD',0xA5),
    ('OpenBSD',0xA6),
    ('MacOS_X',0xA8),
    ('NetBSD',0xA9),
    ('MacOS_X_Boot',0xAB),
    ('BSDI',0xB7),
    ('BSDI_SWAP',0xB8),
    ('EFI_GPT_DISK',0xEE),
    ('EFI_SYSTEM_PARTITION',0xEF),
    ('VMWARE_FILESYSTEM',0xFB),
    ('VMWARE_SWAp',0xFC) ]
   
PARTITION_TYPE = dict(PartitionType+[(e[1], e[0]) for e in PartitionType])

ENDING_CHS_ADDRESS = 0x000000
STARTING_LBA_ADDRESS = 0x00000000
SIZE_IN_SECTOR = 0x00000000
