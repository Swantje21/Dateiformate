<!--
author:  Swantje Piotrowski, Lukas Eweleit, Erik Stoffer, Penelope Stibane, Caroline Beckmann, Arnold A. Willemer

email:    s.piotrowski@email.uni-kiel.de, stu217721@mail.uni-kiel.de, stu201059@mail.uni-kiel.de, stu210544@mail.uni-kiel.de, stu204392@mail.uni-kiel.de

version:  0.0.1

@icon: https://www.uni-kiel.de/ps/cgi-bin/logos/files/cau/norm-de/cau-norm-de-lilagrey-rgb-0720.png

language: de

narrator: Deutsch Female, Male

comment: Der digitale Baustein zu Digital Literacy  möchte Studierende  einen Überblick über künftige Schlüsselqualifikationen ermöglichen. Sie sollen verstehen, welche Kompetenzen künftige Berufs- und Arbeitsfelder erfordern und in der Lage sein, Digital Literacy in einem Lernprozess zu erfahren und zu beurteilen. Nach dieser Lerneinheit sollen Studierende  differenziert und reflektiert Tools und Software anwenden können.

 Den Studierenden sollen die Vorteile des kollaborativen Arbeitens als Teil der Digital Literacy näher gebracht werden. Hierbei steht insbesondere der Anbieter "cryptpad" im Fokus, dessen Funktionsweise anhand einzelner Foto- und Videosequenzen veranschaulicht wird. Am Ende dieses Abschnittes sollen die Studierenden die Vorzüge von digital-kollaborativen Arbeiten kennen und die grundsätzliche Bedienung des Tools cryptpad verstanden haben.

Ziel ist die Präsentation von Techniken und Instrumenten der digitalen
Literaturrecherche sowie Möglichkeiten der Literaturverwaltung.

Leitfaden zum Erstellen einer Formatvorlage in Word

base: https://cloudlab-olathub.rz.uni-kiel.de/user/suzuv062/106513175450593/liascript-preview/
-->

# Dateitypen (Arbeitstitel)

<h3>Inhalt</h3>

[**Allgemeine Informationen**](#2)

[**Textbasierte Dateiformate**] (#8)

[**Ton, Bild, Video**](#13)

[**Karten**](#17)

[**Recherche**](#19)







## Allgemeine Informationen

{{0-2}}Eine der wichtigsten Funktionen von Computern ist die Fähigkeit, sich etwas zu merken - wir sprechen vom **Speichern**. Computer bewerkstelligen dies, in dem sie Daten als magnetische Ladungen auf Festplatten speichern. Weil unterschiedliche Spannungen oder Ladungen schnell verfälscht werden und Daten daruch unleserlich werden könnten[^1](Man denke nur an Spannungsabfälle oder magnetische Einflüsse von außen, die das Ablesen oder Übertragen beeinflussen könnten und den gesamten Datenfluss durcheinanderbringen. Es ist hier also viel einfacher, nur mit zwei Zuständen zu arbeiten. Dabei ist es natürlich effektiver, pro Einheit so viele Zustände wie möglich zu verwenden. Dies ist jedoch etwas, das sich nur Quantencomputer verlässlich zu Nutze machen können. LINK), begrenzt man sich in der Regel auf zwei Zustände: **Ein** und **Aus**, welche wieder um **1** und **0** repräsentieren. Diese können entweder ausgelesen oder verändert werden. 

{{1-2}} Diese kleinsten Einheiten sind die berühmten **Bits**.

{{2-4}}
**************
Doch wie kann aus einfachen Ladungen ein Text, Bild oder Ähnliches Entstehen? 
Die Lösung liegt auf der Hand: es werden mehrere Bits mit einander kombiniert.
Dabei hat sich die Verwendung von **acht Bits** als erstes durchgesetzt und wurde auf den Namen **Byte** getauft.

{{3}} Um die Zählweise des Binären Systems zu verdeutlichen ist hier ein kleines Beispiel (interagiere mit dem Element): 
<script input="number" value="22" min="0" max="1000000">
let i = @input // direct usage as a number
let j = (@input >>> 0).toString(2)

i + " = " + j
</script>

************

<h3>Text vs Binär</h3> 

In ihrer Organisationsform unterscheiden sich Dateien jetzt in zwei Arten.
Die einen halten sich strikt an eine Aufteilung in 8er-Blöcke, also Bytes, in der Regel um Text zu codieren[^2](In Wirklichkeit gibt es viele Textformate, die auch Zeichen wie 'A' mit dem Binärcode '00000000' abenfalls als '0' darstellen, um Speicherplatz zu schonen.)
Hier ist ein beispiel, wie aus Binärem Code Buchstaben werden: 
<script input="number" value="65" min="33" max="126">
let i = @input
let j = (@input >>> 0).toString(2)
let k = String.fromCharCode(i)

i + " = " + j + " = " + k
</script>



### Sinn von unterschiedlichen Formaten

(Infotext)


### Wie werden unterschiedliche Formate im selben System gespeichert? 

(Infotext)



### Wie unterscheiden sie sich?

(Infotext)


### Warum die Endung eine Rolle spielt!

(Infotext)


### Was tun bei unbekannten Formaten? 

(Infotext)




<!--> Ende Abschnitt <-->

## Textbasierte Dateiformate

(Infotext)


### TXT – Mutter aller Textverarbeitung

(Infotext)



### RTF, MD, DOCX, ODT, PAGES — Informationen für Menschen aufbereiten

(Infotext)



### CSV, XML, JSON, HTML — Informationen für Computer aufbereiten

(Infotext)



### PDFs — möglicher Exkurs

(Infotext)






<!--> Ende Abschnitt <-->

## Ton, Bild, Video

(Infotext)

### WAV, MP3 — Ton und Tonqualität

(Infotext)



### RAW, JPEG, PNG — Bild und Bildqualität

(Infotext)



### MP4, MOV — Bild und Ton vereint

(Infotext)



<!--> Ende Abschnitt <-->

## Karten

(Infotext)

### unklar...

(Infotext)



<!--> Ende Abschnitt <-->

## Recherche

(Infotext)

### Wo finde ich Dateiformate? — Einschlägige Webseiten

(Infotext)



### Worauf man achten sollte:

(Infotext)

#### (Plattform-)Kompatibilität

(Infotext)



#### Lebensdauer (Wie alt? Wie langlebig?)

(Infotext)



#### Speichergröße / Ressourcenmanagement

(Infotext)



#### Updates / Support

(Infotext)

<!--> Ende Abschnitt <-->





