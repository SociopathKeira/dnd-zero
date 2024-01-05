import uuid
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


# Create your models here.

class Character(models.Model):

    # Races and Classes
    # Races
    HUMAN = 'HMN'
    DWARF = 'DWF'
    ELF = 'ELF'
    HALF_ELF = 'HEF'
    HALFLING = 'HFG'
    DRAGONBORN = 'DRB'
    GNOME = 'GNM'
    HALF_ORC = 'HOR'
    TIEFLING = 'TFG'

    RACE_CHOICES = [
        (HUMAN, 'Human'),
        (DWARF, 'Dwarf'),
        (ELF, 'Elf'),
        (HALF_ELF, 'Half Elf'),
        (DRAGONBORN, 'Dragonborn'),
        (GNOME, 'Gnome'),
        (HALF_ORC, 'HOR'),
        (TIEFLING, 'Tiefling'),
    ]

    # Classes
    ARTIFICER = 'ART'
    BARBARIAN = 'BAR'
    BARD = 'BAR'
    CLERIC = 'CLR'
    DRUID = 'DRD'
    FIGHTER = 'FGT'
    MONK = 'MNK'
    PALADIN = 'PLD'
    RANGER = 'RNG'
    ROGUE = 'ROG'
    SORCERER = 'SRC'
    WARLOCK = 'WRC'
    WIZARD = 'WZD'

    CLASS_CHOICES = [
        (ARTIFICER, 'Artificer'),
        (BARBARIAN, 'Barbarian'),
        (BARD, 'Bard'),
        (CLERIC, 'Cleric'),
        (DRUID, 'Druid'),
        (FIGHTER, 'Fighter'),
        (MONK, 'Monk'),
        (PALADIN, 'Paladin'),
        (RANGER, 'Ranger'),
        (ROGUE, 'Rogue'),
        (SORCERER, 'Sorcerer'),
        (WARLOCK, 'Warlock'),
        (WIZARD, 'Wizard')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    master = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=20, help_text="Enter your character's name")
    race = models.CharField(max_length=20, choices=RACE_CHOICES)
    character_class = models.CharField(max_length=20, choices=CLASS_CHOICES)

    level = models.IntegerField(default=1)
    experience_points = models.IntegerField(default=0)

    hp = models.IntegerField(default=10, validators=[MinValueValidator(1)])
    max_hp = models.IntegerField(default=10, validators=[MinValueValidator(1)])

    strength = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    dexterity = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    constitution = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    intelligence = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    wisdom = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    charisma = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])

    story1 = models.CharField(max_length=1000, help_text="What is your story?")
    story2 = models.CharField(max_length=1000, help_text="What is your story?")
    story3 = models.CharField(max_length=1000, help_text="What is your story?")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('character_detail', args=[str(self.id)])

