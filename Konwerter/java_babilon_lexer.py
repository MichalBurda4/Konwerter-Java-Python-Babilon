# Generated from java_babilon_lexer.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2h")
        buf.write("\u030b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\4h\th\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"")
        buf.write("\3#\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)")
        buf.write("\3*\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3")
        buf.write(":\3:\3;\3;\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3?\3?\7?\u01ef")
        buf.write("\n?\f?\16?\u01f2\13?\3?\3?\3@\3@\3@\3@\7@\u01fa\n@\f@")
        buf.write("\16@\u01fd\13@\3@\3@\3@\3@\3@\3A\3A\3B\3B\3C\3C\3C\7C")
        buf.write("\u020b\nC\fC\16C\u020e\13C\5C\u0210\nC\3D\3D\3D\3D\3E")
        buf.write("\6E\u0217\nE\rE\16E\u0218\3E\3E\7E\u021d\nE\fE\16E\u0220")
        buf.write("\13E\3F\3F\3F\3F\3F\3F\3G\3G\3G\3G\3G\3H\3H\7H\u022f\n")
        buf.write("H\fH\16H\u0232\13H\3H\3H\3I\3I\3I\3I\3I\3I\3I\3J\3J\3")
        buf.write("J\3J\3J\3J\3J\3K\3K\3K\3K\3K\3L\3L\3L\3L\3L\3L\3M\3M\3")
        buf.write("M\3M\3M\3N\3N\3N\3N\3N\3O\3O\3O\3O\3O\3O\3O\3O\3P\3P\3")
        buf.write("P\3P\3P\3P\3P\3P\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3R\3R\3R\3R\3R\3")
        buf.write("R\3S\3S\3S\3S\3S\3T\3T\3T\3T\3T\3T\3U\3U\3U\3U\3U\3V\3")
        buf.write("V\3V\3V\3V\3V\3V\3V\3V\3V\3W\3W\3W\3W\3W\3W\3W\3W\3X\3")
        buf.write("X\3X\3X\3X\3X\3X\3X\3X\3X\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3")
        buf.write("Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3")
        buf.write("Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3[\3[\3[\3[\3[\3[\3[\3[\3\\")
        buf.write("\3\\\3\\\3\\\3\\\3]\3]\7]\u02d5\n]\f]\16]\u02d8\13]\3")
        buf.write("^\3^\3^\3^\3^\3_\3_\3_\3_\3_\3_\3`\3`\3`\3`\3`\3a\3a\3")
        buf.write("b\6b\u02ed\nb\rb\16b\u02ee\3c\6c\u02f2\nc\rc\16c\u02f3")
        buf.write("\3c\3c\6c\u02f8\nc\rc\16c\u02f9\3d\3d\3e\3e\3f\3f\3g\3")
        buf.write("g\3g\3h\6h\u0306\nh\rh\16h\u0307\3h\3h\3\u01fb\2i\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w")
        buf.write("=y>{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F\u008b")
        buf.write("G\u008dH\u008fI\u0091J\u0093K\u0095L\u0097M\u0099N\u009b")
        buf.write("O\u009dP\u009fQ\u00a1R\u00a3S\u00a5T\u00a7U\u00a9V\u00ab")
        buf.write("W\u00adX\u00afY\u00b1Z\u00b3[\u00b5\\\u00b7]\u00b9^\u00bb")
        buf.write("_\u00bd`\u00bfa\u00c1\2\u00c3b\u00c5c\u00c7d\u00c9e\u00cb")
        buf.write("f\u00cdg\u00cfh\3\2\t\4\2\f\f\17\17\3\2\63;\3\2\62;\6")
        buf.write("\2\f\f\17\17$$^^\4\2C\\c|\6\2\62;C\\aac|\5\2\13\f\16\17")
        buf.write("\"\"\2\u0315\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2")
        buf.write("\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab")
        buf.write("\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2")
        buf.write("\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9")
        buf.write("\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2")
        buf.write("\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2\2\2\u00c9")
        buf.write("\3\2\2\2\2\u00cb\3\2\2\2\2\u00cd\3\2\2\2\2\u00cf\3\2\2")
        buf.write("\2\3\u00d1\3\2\2\2\5\u00d7\3\2\2\2\7\u00de\3\2\2\2\t\u00e6")
        buf.write("\3\2\2\2\13\u00f0\3\2\2\2\r\u00f3\3\2\2\2\17\u00f6\3\2")
        buf.write("\2\2\21\u00fb\3\2\2\2\23\u0102\3\2\2\2\25\u0108\3\2\2")
        buf.write("\2\27\u010e\3\2\2\2\31\u0112\3\2\2\2\33\u0117\3\2\2\2")
        buf.write("\35\u0120\3\2\2\2\37\u0125\3\2\2\2!\u012c\3\2\2\2#\u0133")
        buf.write("\3\2\2\2%\u0139\3\2\2\2\'\u0142\3\2\2\2)\u014a\3\2\2\2")
        buf.write("+\u0152\3\2\2\2-\u015d\3\2\2\2/\u0167\3\2\2\2\61\u016e")
        buf.write("\3\2\2\2\63\u0172\3\2\2\2\65\u0178\3\2\2\2\67\u0180\3")
        buf.write("\2\2\29\u0184\3\2\2\2;\u0189\3\2\2\2=\u0190\3\2\2\2?\u0197")
        buf.write("\3\2\2\2A\u019f\3\2\2\2C\u01a3\3\2\2\2E\u01a5\3\2\2\2")
        buf.write("G\u01a7\3\2\2\2I\u01a9\3\2\2\2K\u01ab\3\2\2\2M\u01ae\3")
        buf.write("\2\2\2O\u01b0\3\2\2\2Q\u01b3\3\2\2\2S\u01b6\3\2\2\2U\u01b9")
        buf.write("\3\2\2\2W\u01bb\3\2\2\2Y\u01bd\3\2\2\2[\u01bf\3\2\2\2")
        buf.write("]\u01c2\3\2\2\2_\u01c5\3\2\2\2a\u01c7\3\2\2\2c\u01ca\3")
        buf.write("\2\2\2e\u01cd\3\2\2\2g\u01d0\3\2\2\2i\u01d3\3\2\2\2k\u01d6")
        buf.write("\3\2\2\2m\u01d8\3\2\2\2o\u01da\3\2\2\2q\u01dc\3\2\2\2")
        buf.write("s\u01de\3\2\2\2u\u01e0\3\2\2\2w\u01e2\3\2\2\2y\u01e4\3")
        buf.write("\2\2\2{\u01e7\3\2\2\2}\u01ea\3\2\2\2\177\u01f5\3\2\2\2")
        buf.write("\u0081\u0203\3\2\2\2\u0083\u0205\3\2\2\2\u0085\u020f\3")
        buf.write("\2\2\2\u0087\u0211\3\2\2\2\u0089\u0216\3\2\2\2\u008b\u0221")
        buf.write("\3\2\2\2\u008d\u0227\3\2\2\2\u008f\u022c\3\2\2\2\u0091")
        buf.write("\u0235\3\2\2\2\u0093\u023c\3\2\2\2\u0095\u0243\3\2\2\2")
        buf.write("\u0097\u0248\3\2\2\2\u0099\u024e\3\2\2\2\u009b\u0253\3")
        buf.write("\2\2\2\u009d\u0258\3\2\2\2\u009f\u0260\3\2\2\2\u00a1\u0268")
        buf.write("\3\2\2\2\u00a3\u026f\3\2\2\2\u00a5\u0275\3\2\2\2\u00a7")
        buf.write("\u027a\3\2\2\2\u00a9\u0280\3\2\2\2\u00ab\u0285\3\2\2\2")
        buf.write("\u00ad\u028f\3\2\2\2\u00af\u0297\3\2\2\2\u00b1\u02a1\3")
        buf.write("\2\2\2\u00b3\u02b2\3\2\2\2\u00b5\u02c5\3\2\2\2\u00b7\u02cd")
        buf.write("\3\2\2\2\u00b9\u02d2\3\2\2\2\u00bb\u02d9\3\2\2\2\u00bd")
        buf.write("\u02de\3\2\2\2\u00bf\u02e4\3\2\2\2\u00c1\u02e9\3\2\2\2")
        buf.write("\u00c3\u02ec\3\2\2\2\u00c5\u02f1\3\2\2\2\u00c7\u02fb\3")
        buf.write("\2\2\2\u00c9\u02fd\3\2\2\2\u00cb\u02ff\3\2\2\2\u00cd\u0301")
        buf.write("\3\2\2\2\u00cf\u0305\3\2\2\2\u00d1\u00d2\7e\2\2\u00d2")
        buf.write("\u00d3\7n\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5\7u\2\2\u00d5")
        buf.write("\u00d6\7u\2\2\u00d6\4\3\2\2\2\u00d7\u00d8\7r\2\2\u00d8")
        buf.write("\u00d9\7w\2\2\u00d9\u00da\7d\2\2\u00da\u00db\7n\2\2\u00db")
        buf.write("\u00dc\7k\2\2\u00dc\u00dd\7e\2\2\u00dd\6\3\2\2\2\u00de")
        buf.write("\u00df\7r\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1\7k\2\2\u00e1")
        buf.write("\u00e2\7x\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4\7v\2\2\u00e4")
        buf.write("\u00e5\7g\2\2\u00e5\b\3\2\2\2\u00e6\u00e7\7r\2\2\u00e7")
        buf.write("\u00e8\7t\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea\7v\2\2\u00ea")
        buf.write("\u00eb\7g\2\2\u00eb\u00ec\7e\2\2\u00ec\u00ed\7v\2\2\u00ed")
        buf.write("\u00ee\7g\2\2\u00ee\u00ef\7f\2\2\u00ef\n\3\2\2\2\u00f0")
        buf.write("\u00f1\7k\2\2\u00f1\u00f2\7h\2\2\u00f2\f\3\2\2\2\u00f3")
        buf.write("\u00f4\7f\2\2\u00f4\u00f5\7q\2\2\u00f5\16\3\2\2\2\u00f6")
        buf.write("\u00f7\7g\2\2\u00f7\u00f8\7n\2\2\u00f8\u00f9\7u\2\2\u00f9")
        buf.write("\u00fa\7g\2\2\u00fa\20\3\2\2\2\u00fb\u00fc\7t\2\2\u00fc")
        buf.write("\u00fd\7g\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7w\2\2\u00ff")
        buf.write("\u0100\7t\2\2\u0100\u0101\7p\2\2\u0101\22\3\2\2\2\u0102")
        buf.write("\u0103\7d\2\2\u0103\u0104\7t\2\2\u0104\u0105\7g\2\2\u0105")
        buf.write("\u0106\7c\2\2\u0106\u0107\7m\2\2\u0107\24\3\2\2\2\u0108")
        buf.write("\u0109\7y\2\2\u0109\u010a\7j\2\2\u010a\u010b\7k\2\2\u010b")
        buf.write("\u010c\7n\2\2\u010c\u010d\7g\2\2\u010d\26\3\2\2\2\u010e")
        buf.write("\u010f\7h\2\2\u010f\u0110\7q\2\2\u0110\u0111\7t\2\2\u0111")
        buf.write("\30\3\2\2\2\u0112\u0113\7g\2\2\u0113\u0114\7p\2\2\u0114")
        buf.write("\u0115\7w\2\2\u0115\u0116\7o\2\2\u0116\32\3\2\2\2\u0117")
        buf.write("\u0118\7e\2\2\u0118\u0119\7q\2\2\u0119\u011a\7p\2\2\u011a")
        buf.write("\u011b\7v\2\2\u011b\u011c\7k\2\2\u011c\u011d\7p\2\2\u011d")
        buf.write("\u011e\7w\2\2\u011e\u011f\7g\2\2\u011f\34\3\2\2\2\u0120")
        buf.write("\u0121\7e\2\2\u0121\u0122\7c\2\2\u0122\u0123\7u\2\2\u0123")
        buf.write("\u0124\7g\2\2\u0124\36\3\2\2\2\u0125\u0126\7u\2\2\u0126")
        buf.write("\u0127\7y\2\2\u0127\u0128\7k\2\2\u0128\u0129\7v\2\2\u0129")
        buf.write("\u012a\7e\2\2\u012a\u012b\7j\2\2\u012b \3\2\2\2\u012c")
        buf.write("\u012d\7u\2\2\u012d\u012e\7v\2\2\u012e\u012f\7c\2\2\u012f")
        buf.write("\u0130\7v\2\2\u0130\u0131\7k\2\2\u0131\u0132\7e\2\2\u0132")
        buf.write("\"\3\2\2\2\u0133\u0134\7h\2\2\u0134\u0135\7k\2\2\u0135")
        buf.write("\u0136\7p\2\2\u0136\u0137\7c\2\2\u0137\u0138\7n\2\2\u0138")
        buf.write("$\3\2\2\2\u0139\u013a\7c\2\2\u013a\u013b\7d\2\2\u013b")
        buf.write("\u013c\7u\2\2\u013c\u013d\7v\2\2\u013d\u013e\7t\2\2\u013e")
        buf.write("\u013f\7c\2\2\u013f\u0140\7e\2\2\u0140\u0141\7v\2\2\u0141")
        buf.write("&\3\2\2\2\u0142\u0143\7f\2\2\u0143\u0144\7g\2\2\u0144")
        buf.write("\u0145\7h\2\2\u0145\u0146\7c\2\2\u0146\u0147\7w\2\2\u0147")
        buf.write("\u0148\7n\2\2\u0148\u0149\7v\2\2\u0149(\3\2\2\2\u014a")
        buf.write("\u014b\7g\2\2\u014b\u014c\7z\2\2\u014c\u014d\7v\2\2\u014d")
        buf.write("\u014e\7g\2\2\u014e\u014f\7p\2\2\u014f\u0150\7f\2\2\u0150")
        buf.write("\u0151\7u\2\2\u0151*\3\2\2\2\u0152\u0153\7k\2\2\u0153")
        buf.write("\u0154\7o\2\2\u0154\u0155\7r\2\2\u0155\u0156\7n\2\2\u0156")
        buf.write("\u0157\7g\2\2\u0157\u0158\7o\2\2\u0158\u0159\7g\2\2\u0159")
        buf.write("\u015a\7p\2\2\u015a\u015b\7v\2\2\u015b\u015c\7u\2\2\u015c")
        buf.write(",\3\2\2\2\u015d\u015e\7x\2\2\u015e\u015f\7q\2\2\u015f")
        buf.write("\u0160\7n\2\2\u0160\u0161\7c\2\2\u0161\u0162\7v\2\2\u0162")
        buf.write("\u0163\7c\2\2\u0163\u0164\7k\2\2\u0164\u0165\7n\2\2\u0165")
        buf.write("\u0166\7g\2\2\u0166.\3\2\2\2\u0167\u0168\7v\2\2\u0168")
        buf.write("\u0169\7j\2\2\u0169\u016a\7t\2\2\u016a\u016b\7q\2\2\u016b")
        buf.write("\u016c\7y\2\2\u016c\u016d\7u\2\2\u016d\60\3\2\2\2\u016e")
        buf.write("\u016f\7v\2\2\u016f\u0170\7t\2\2\u0170\u0171\7{\2\2\u0171")
        buf.write("\62\3\2\2\2\u0172\u0173\7e\2\2\u0173\u0174\7c\2\2\u0174")
        buf.write("\u0175\7v\2\2\u0175\u0176\7e\2\2\u0176\u0177\7j\2\2\u0177")
        buf.write("\64\3\2\2\2\u0178\u0179\7h\2\2\u0179\u017a\7k\2\2\u017a")
        buf.write("\u017b\7p\2\2\u017b\u017c\7c\2\2\u017c\u017d\7n\2\2\u017d")
        buf.write("\u017e\7n\2\2\u017e\u017f\7{\2\2\u017f\66\3\2\2\2\u0180")
        buf.write("\u0181\7p\2\2\u0181\u0182\7g\2\2\u0182\u0183\7y\2\2\u0183")
        buf.write("8\3\2\2\2\u0184\u0185\7v\2\2\u0185\u0186\7j\2\2\u0186")
        buf.write("\u0187\7k\2\2\u0187\u0188\7u\2\2\u0188:\3\2\2\2\u0189")
        buf.write("\u018a\7c\2\2\u018a\u018b\7u\2\2\u018b\u018c\7u\2\2\u018c")
        buf.write("\u018d\7g\2\2\u018d\u018e\7t\2\2\u018e\u018f\7v\2\2\u018f")
        buf.write("<\3\2\2\2\u0190\u0191\7k\2\2\u0191\u0192\7o\2\2\u0192")
        buf.write("\u0193\7r\2\2\u0193\u0194\7q\2\2\u0194\u0195\7t\2\2\u0195")
        buf.write("\u0196\7v\2\2\u0196>\3\2\2\2\u0197\u0198\7r\2\2\u0198")
        buf.write("\u0199\7c\2\2\u0199\u019a\7e\2\2\u019a\u019b\7m\2\2\u019b")
        buf.write("\u019c\7c\2\2\u019c\u019d\7i\2\2\u019d\u019e\7g\2\2\u019e")
        buf.write("@\3\2\2\2\u019f\u01a0\7c\2\2\u01a0\u01a1\7f\2\2\u01a1")
        buf.write("\u01a2\7f\2\2\u01a2B\3\2\2\2\u01a3\u01a4\7-\2\2\u01a4")
        buf.write("D\3\2\2\2\u01a5\u01a6\7/\2\2\u01a6F\3\2\2\2\u01a7\u01a8")
        buf.write("\7,\2\2\u01a8H\3\2\2\2\u01a9\u01aa\7\61\2\2\u01aaJ\3\2")
        buf.write("\2\2\u01ab\u01ac\7?\2\2\u01ac\u01ad\7?\2\2\u01adL\3\2")
        buf.write("\2\2\u01ae\u01af\7?\2\2\u01afN\3\2\2\2\u01b0\u01b1\7#")
        buf.write("\2\2\u01b1\u01b2\7?\2\2\u01b2P\3\2\2\2\u01b3\u01b4\7~")
        buf.write("\2\2\u01b4\u01b5\7~\2\2\u01b5R\3\2\2\2\u01b6\u01b7\7(")
        buf.write("\2\2\u01b7\u01b8\7(\2\2\u01b8T\3\2\2\2\u01b9\u01ba\7\'")
        buf.write("\2\2\u01baV\3\2\2\2\u01bb\u01bc\7>\2\2\u01bcX\3\2\2\2")
        buf.write("\u01bd\u01be\7@\2\2\u01beZ\3\2\2\2\u01bf\u01c0\7@\2\2")
        buf.write("\u01c0\u01c1\7?\2\2\u01c1\\\3\2\2\2\u01c2\u01c3\7>\2\2")
        buf.write("\u01c3\u01c4\7?\2\2\u01c4^\3\2\2\2\u01c5\u01c6\7#\2\2")
        buf.write("\u01c6`\3\2\2\2\u01c7\u01c8\7-\2\2\u01c8\u01c9\7?\2\2")
        buf.write("\u01c9b\3\2\2\2\u01ca\u01cb\7/\2\2\u01cb\u01cc\7?\2\2")
        buf.write("\u01ccd\3\2\2\2\u01cd\u01ce\7,\2\2\u01ce\u01cf\7?\2\2")
        buf.write("\u01cff\3\2\2\2\u01d0\u01d1\7\61\2\2\u01d1\u01d2\7?\2")
        buf.write("\2\u01d2h\3\2\2\2\u01d3\u01d4\7\'\2\2\u01d4\u01d5\7?\2")
        buf.write("\2\u01d5j\3\2\2\2\u01d6\u01d7\7*\2\2\u01d7l\3\2\2\2\u01d8")
        buf.write("\u01d9\7+\2\2\u01d9n\3\2\2\2\u01da\u01db\7}\2\2\u01db")
        buf.write("p\3\2\2\2\u01dc\u01dd\7\177\2\2\u01ddr\3\2\2\2\u01de\u01df")
        buf.write("\7=\2\2\u01dft\3\2\2\2\u01e0\u01e1\7]\2\2\u01e1v\3\2\2")
        buf.write("\2\u01e2\u01e3\7_\2\2\u01e3x\3\2\2\2\u01e4\u01e5\7-\2")
        buf.write("\2\u01e5\u01e6\7-\2\2\u01e6z\3\2\2\2\u01e7\u01e8\7/\2")
        buf.write("\2\u01e8\u01e9\7/\2\2\u01e9|\3\2\2\2\u01ea\u01eb\7\61")
        buf.write("\2\2\u01eb\u01ec\7\61\2\2\u01ec\u01f0\3\2\2\2\u01ed\u01ef")
        buf.write("\n\2\2\2\u01ee\u01ed\3\2\2\2\u01ef\u01f2\3\2\2\2\u01f0")
        buf.write("\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f3\3\2\2\2")
        buf.write("\u01f2\u01f0\3\2\2\2\u01f3\u01f4\b?\2\2\u01f4~\3\2\2\2")
        buf.write("\u01f5\u01f6\7\61\2\2\u01f6\u01f7\7,\2\2\u01f7\u01fb\3")
        buf.write("\2\2\2\u01f8\u01fa\13\2\2\2\u01f9\u01f8\3\2\2\2\u01fa")
        buf.write("\u01fd\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fb\u01f9\3\2\2\2")
        buf.write("\u01fc\u01fe\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fe\u01ff\7")
        buf.write(",\2\2\u01ff\u0200\7\61\2\2\u0200\u0201\3\2\2\2\u0201\u0202")
        buf.write("\b@\2\2\u0202\u0080\3\2\2\2\u0203\u0204\7\f\2\2\u0204")
        buf.write("\u0082\3\2\2\2\u0205\u0206\7\13\2\2\u0206\u0084\3\2\2")
        buf.write("\2\u0207\u0210\7\62\2\2\u0208\u020c\t\3\2\2\u0209\u020b")
        buf.write("\t\4\2\2\u020a\u0209\3\2\2\2\u020b\u020e\3\2\2\2\u020c")
        buf.write("\u020a\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u0210\3\2\2\2")
        buf.write("\u020e\u020c\3\2\2\2\u020f\u0207\3\2\2\2\u020f\u0208\3")
        buf.write("\2\2\2\u0210\u0086\3\2\2\2\u0211\u0212\7k\2\2\u0212\u0213")
        buf.write("\7p\2\2\u0213\u0214\7v\2\2\u0214\u0088\3\2\2\2\u0215\u0217")
        buf.write("\t\4\2\2\u0216\u0215\3\2\2\2\u0217\u0218\3\2\2\2\u0218")
        buf.write("\u0216\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u021a\3\2\2\2")
        buf.write("\u021a\u021e\7\60\2\2\u021b\u021d\t\4\2\2\u021c\u021b")
        buf.write("\3\2\2\2\u021d\u0220\3\2\2\2\u021e\u021c\3\2\2\2\u021e")
        buf.write("\u021f\3\2\2\2\u021f\u008a\3\2\2\2\u0220\u021e\3\2\2\2")
        buf.write("\u0221\u0222\7h\2\2\u0222\u0223\7n\2\2\u0223\u0224\7q")
        buf.write("\2\2\u0224\u0225\7c\2\2\u0225\u0226\7v\2\2\u0226\u008c")
        buf.write("\3\2\2\2\u0227\u0228\7x\2\2\u0228\u0229\7q\2\2\u0229\u022a")
        buf.write("\7k\2\2\u022a\u022b\7f\2\2\u022b\u008e\3\2\2\2\u022c\u0230")
        buf.write("\7$\2\2\u022d\u022f\n\5\2\2\u022e\u022d\3\2\2\2\u022f")
        buf.write("\u0232\3\2\2\2\u0230\u022e\3\2\2\2\u0230\u0231\3\2\2\2")
        buf.write("\u0231\u0233\3\2\2\2\u0232\u0230\3\2\2\2\u0233\u0234\7")
        buf.write("$\2\2\u0234\u0090\3\2\2\2\u0235\u0236\7U\2\2\u0236\u0237")
        buf.write("\7v\2\2\u0237\u0238\7t\2\2\u0238\u0239\7k\2\2\u0239\u023a")
        buf.write("\7p\2\2\u023a\u023b\7i\2\2\u023b\u0092\3\2\2\2\u023c\u023d")
        buf.write("\7f\2\2\u023d\u023e\7q\2\2\u023e\u023f\7w\2\2\u023f\u0240")
        buf.write("\7d\2\2\u0240\u0241\7n\2\2\u0241\u0242\7g\2\2\u0242\u0094")
        buf.write("\3\2\2\2\u0243\u0244\7n\2\2\u0244\u0245\7q\2\2\u0245\u0246")
        buf.write("\7p\2\2\u0246\u0247\7i\2\2\u0247\u0096\3\2\2\2\u0248\u0249")
        buf.write("\7u\2\2\u0249\u024a\7j\2\2\u024a\u024b\7q\2\2\u024b\u024c")
        buf.write("\7t\2\2\u024c\u024d\7v\2\2\u024d\u0098\3\2\2\2\u024e\u024f")
        buf.write("\7d\2\2\u024f\u0250\7{\2\2\u0250\u0251\7v\2\2\u0251\u0252")
        buf.write("\7g\2\2\u0252\u009a\3\2\2\2\u0253\u0254\7e\2\2\u0254\u0255")
        buf.write("\7j\2\2\u0255\u0256\7c\2\2\u0256\u0257\7t\2\2\u0257\u009c")
        buf.write("\3\2\2\2\u0258\u0259\7d\2\2\u0259\u025a\7q\2\2\u025a\u025b")
        buf.write("\7q\2\2\u025b\u025c\7n\2\2\u025c\u025d\7g\2\2\u025d\u025e")
        buf.write("\7c\2\2\u025e\u025f\7p\2\2\u025f\u009e\3\2\2\2\u0260\u0261")
        buf.write("\7K\2\2\u0261\u0262\7p\2\2\u0262\u0263\7v\2\2\u0263\u0264")
        buf.write("\7g\2\2\u0264\u0265\7i\2\2\u0265\u0266\7g\2\2\u0266\u0267")
        buf.write("\7t\2\2\u0267\u00a0\3\2\2\2\u0268\u0269\7F\2\2\u0269\u026a")
        buf.write("\7q\2\2\u026a\u026b\7w\2\2\u026b\u026c\7d\2\2\u026c\u026d")
        buf.write("\7n\2\2\u026d\u026e\7g\2\2\u026e\u00a2\3\2\2\2\u026f\u0270")
        buf.write("\7H\2\2\u0270\u0271\7n\2\2\u0271\u0272\7q\2\2\u0272\u0273")
        buf.write("\7c\2\2\u0273\u0274\7v\2\2\u0274\u00a4\3\2\2\2\u0275\u0276")
        buf.write("\7N\2\2\u0276\u0277\7q\2\2\u0277\u0278\7p\2\2\u0278\u0279")
        buf.write("\7i\2\2\u0279\u00a6\3\2\2\2\u027a\u027b\7U\2\2\u027b\u027c")
        buf.write("\7j\2\2\u027c\u027d\7q\2\2\u027d\u027e\7t\2\2\u027e\u027f")
        buf.write("\7v\2\2\u027f\u00a8\3\2\2\2\u0280\u0281\7D\2\2\u0281\u0282")
        buf.write("\7{\2\2\u0282\u0283\7v\2\2\u0283\u0284\7g\2\2\u0284\u00aa")
        buf.write("\3\2\2\2\u0285\u0286\7E\2\2\u0286\u0287\7j\2\2\u0287\u0288")
        buf.write("\7c\2\2\u0288\u0289\7t\2\2\u0289\u028a\7c\2\2\u028a\u028b")
        buf.write("\7e\2\2\u028b\u028c\7v\2\2\u028c\u028d\7g\2\2\u028d\u028e")
        buf.write("\7t\2\2\u028e\u00ac\3\2\2\2\u028f\u0290\7D\2\2\u0290\u0291")
        buf.write("\7q\2\2\u0291\u0292\7q\2\2\u0292\u0293\7n\2\2\u0293\u0294")
        buf.write("\7g\2\2\u0294\u0295\7c\2\2\u0295\u0296\7p\2\2\u0296\u00ae")
        buf.write("\3\2\2\2\u0297\u0298\7C\2\2\u0298\u0299\7t\2\2\u0299\u029a")
        buf.write("\7t\2\2\u029a\u029b\7c\2\2\u029b\u029c\7{\2\2\u029c\u029d")
        buf.write("\7N\2\2\u029d\u029e\7k\2\2\u029e\u029f\7u\2\2\u029f\u02a0")
        buf.write("\7v\2\2\u02a0\u00b0\3\2\2\2\u02a1\u02a2\7U\2\2\u02a2\u02a3")
        buf.write("\7{\2\2\u02a3\u02a4\7u\2\2\u02a4\u02a5\7v\2\2\u02a5\u02a6")
        buf.write("\7g\2\2\u02a6\u02a7\7o\2\2\u02a7\u02a8\7\60\2\2\u02a8")
        buf.write("\u02a9\7q\2\2\u02a9\u02aa\7w\2\2\u02aa\u02ab\7v\2\2\u02ab")
        buf.write("\u02ac\7\60\2\2\u02ac\u02ad\7r\2\2\u02ad\u02ae\7t\2\2")
        buf.write("\u02ae\u02af\7k\2\2\u02af\u02b0\7p\2\2\u02b0\u02b1\7v")
        buf.write("\2\2\u02b1\u00b2\3\2\2\2\u02b2\u02b3\7U\2\2\u02b3\u02b4")
        buf.write("\7{\2\2\u02b4\u02b5\7u\2\2\u02b5\u02b6\7v\2\2\u02b6\u02b7")
        buf.write("\7g\2\2\u02b7\u02b8\7o\2\2\u02b8\u02b9\7\60\2\2\u02b9")
        buf.write("\u02ba\7q\2\2\u02ba\u02bb\7w\2\2\u02bb\u02bc\7v\2\2\u02bc")
        buf.write("\u02bd\7\60\2\2\u02bd\u02be\7r\2\2\u02be\u02bf\7t\2\2")
        buf.write("\u02bf\u02c0\7k\2\2\u02c0\u02c1\7p\2\2\u02c1\u02c2\7v")
        buf.write("\2\2\u02c2\u02c3\7n\2\2\u02c3\u02c4\7p\2\2\u02c4\u00b4")
        buf.write("\3\2\2\2\u02c5\u02c6\7U\2\2\u02c6\u02c7\7e\2\2\u02c7\u02c8")
        buf.write("\7c\2\2\u02c8\u02c9\7p\2\2\u02c9\u02ca\7p\2\2\u02ca\u02cb")
        buf.write("\7g\2\2\u02cb\u02cc\7t\2\2\u02cc\u00b6\3\2\2\2\u02cd\u02ce")
        buf.write("\7p\2\2\u02ce\u02cf\7g\2\2\u02cf\u02d0\7z\2\2\u02d0\u02d1")
        buf.write("\7v\2\2\u02d1\u00b8\3\2\2\2\u02d2\u02d6\t\6\2\2\u02d3")
        buf.write("\u02d5\t\7\2\2\u02d4\u02d3\3\2\2\2\u02d5\u02d8\3\2\2\2")
        buf.write("\u02d6\u02d4\3\2\2\2\u02d6\u02d7\3\2\2\2\u02d7\u00ba\3")
        buf.write("\2\2\2\u02d8\u02d6\3\2\2\2\u02d9\u02da\7v\2\2\u02da\u02db")
        buf.write("\7t\2\2\u02db\u02dc\7w\2\2\u02dc\u02dd\7g\2\2\u02dd\u00bc")
        buf.write("\3\2\2\2\u02de\u02df\7h\2\2\u02df\u02e0\7c\2\2\u02e0\u02e1")
        buf.write("\7n\2\2\u02e1\u02e2\7u\2\2\u02e2\u02e3\7g\2\2\u02e3\u00be")
        buf.write("\3\2\2\2\u02e4\u02e5\7p\2\2\u02e5\u02e6\7w\2\2\u02e6\u02e7")
        buf.write("\7n\2\2\u02e7\u02e8\7n\2\2\u02e8\u00c0\3\2\2\2\u02e9\u02ea")
        buf.write("\t\4\2\2\u02ea\u00c2\3\2\2\2\u02eb\u02ed\5\u00c1a\2\u02ec")
        buf.write("\u02eb\3\2\2\2\u02ed\u02ee\3\2\2\2\u02ee\u02ec\3\2\2\2")
        buf.write("\u02ee\u02ef\3\2\2\2\u02ef\u00c4\3\2\2\2\u02f0\u02f2\5")
        buf.write("\u00c1a\2\u02f1\u02f0\3\2\2\2\u02f2\u02f3\3\2\2\2\u02f3")
        buf.write("\u02f1\3\2\2\2\u02f3\u02f4\3\2\2\2\u02f4\u02f5\3\2\2\2")
        buf.write("\u02f5\u02f7\13\2\2\2\u02f6\u02f8\5\u00c1a\2\u02f7\u02f6")
        buf.write("\3\2\2\2\u02f8\u02f9\3\2\2\2\u02f9\u02f7\3\2\2\2\u02f9")
        buf.write("\u02fa\3\2\2\2\u02fa\u00c6\3\2\2\2\u02fb\u02fc\7\60\2")
        buf.write("\2\u02fc\u00c8\3\2\2\2\u02fd\u02fe\7.\2\2\u02fe\u00ca")
        buf.write("\3\2\2\2\u02ff\u0300\7A\2\2\u0300\u00cc\3\2\2\2\u0301")
        buf.write("\u0302\7<\2\2\u0302\u0303\7<\2\2\u0303\u00ce\3\2\2\2\u0304")
        buf.write("\u0306\t\b\2\2\u0305\u0304\3\2\2\2\u0306\u0307\3\2\2\2")
        buf.write("\u0307\u0305\3\2\2\2\u0307\u0308\3\2\2\2\u0308\u0309\3")
        buf.write("\2\2\2\u0309\u030a\bh\2\2\u030a\u00d0\3\2\2\2\17\2\u01f0")
        buf.write("\u01fb\u020c\u020f\u0218\u021e\u0230\u02d6\u02ee\u02f3")
        buf.write("\u02f9\u0307\3\b\2\2")
        return buf.getvalue()


class java_babilon_lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CLASS = 1
    PUBLIC = 2
    PRIVATE = 3
    PROTECTED = 4
    IF = 5
    DO = 6
    ELSE = 7
    RETURN = 8
    BREAK = 9
    WHILE = 10
    FOR = 11
    ENUM = 12
    CONTINUE = 13
    CASE = 14
    SWITCH = 15
    STATIC = 16
    FINAL = 17
    ABSTRACT = 18
    DEFAULT = 19
    EXTENDS = 20
    IMPLEMENTS = 21
    VOLATAILE = 22
    THROWS = 23
    TRY = 24
    CATCH = 25
    FINALLY = 26
    NEW = 27
    THIS = 28
    ASSERT = 29
    IMPORT = 30
    PACKAGE = 31
    ADD = 32
    PLUS = 33
    MINUS = 34
    MULT = 35
    DIV = 36
    EQUAL = 37
    ASSIGN = 38
    NOT_EQUAL = 39
    OR = 40
    AND = 41
    MOD = 42
    LESS = 43
    GREATHER = 44
    GREATHER_EQUAL = 45
    LESS_EQUAL = 46
    LOGICAL_NOT = 47
    ADD_ASSIGN = 48
    SUB_ASSIGN = 49
    MUL_ASSIGN = 50
    DIV_ASSIGN = 51
    MOD_ASSIGN = 52
    LPAREN = 53
    RPAREN = 54
    LBRACE = 55
    RBRACE = 56
    SEMICOLON = 57
    LSQUARE = 58
    RSQUARE = 59
    INCREMENT = 60
    DECREMENT = 61
    SINGLE_LINE_COMMENT = 62
    MULTI_LINE_COMMENT = 63
    NEWLINE = 64
    TAB = 65
    INTEGER = 66
    INTEGER_TOKEN = 67
    FLOAT = 68
    FLOAT_TOKEN = 69
    VOID = 70
    STRING = 71
    STRING_TOKEN = 72
    DOUBLE = 73
    LONG = 74
    SHORT = 75
    BYTE = 76
    CHAR = 77
    BOOLEAN = 78
    INTEGERB = 79
    DOUBLEB = 80
    FLOATB = 81
    LONGB = 82
    SHORTB = 83
    BYTEB = 84
    CHARACTERB = 85
    BOOLEANB = 86
    ARRAY_LIST = 87
    PRINT = 88
    PRINTLN = 89
    SCANNER = 90
    NEXT = 91
    IDENTIFIER = 92
    TRUE = 93
    FALSE = 94
    NULL = 95
    INTEGER_NUMBER = 96
    FLOAT_NUMBER = 97
    DOT = 98
    COMMA = 99
    TERNARY = 100
    THE_DOUBLE_COLON = 101
    WHITESPACE = 102

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'class'", "'public'", "'private'", "'protected'", "'if'", "'do'", 
            "'else'", "'return'", "'break'", "'while'", "'for'", "'enum'", 
            "'continue'", "'case'", "'switch'", "'static'", "'final'", "'abstract'", 
            "'default'", "'extends'", "'implements'", "'volataile'", "'throws'", 
            "'try'", "'catch'", "'finally'", "'new'", "'this'", "'assert'", 
            "'import'", "'package'", "'add'", "'+'", "'-'", "'*'", "'/'", 
            "'=='", "'='", "'!='", "'||'", "'&&'", "'%'", "'<'", "'>'", 
            "'>='", "'<='", "'!'", "'+='", "'-='", "'*='", "'/='", "'%='", 
            "'('", "')'", "'{'", "'}'", "';'", "'['", "']'", "'++'", "'--'", 
            "'\n'", "'\t'", "'int'", "'float'", "'void'", "'String'", "'double'", 
            "'long'", "'short'", "'byte'", "'char'", "'boolean'", "'Integer'", 
            "'Double'", "'Float'", "'Long'", "'Short'", "'Byte'", "'Character'", 
            "'Boolean'", "'ArrayList'", "'System.out.print'", "'System.out.println'", 
            "'Scanner'", "'next'", "'true'", "'false'", "'null'", "'.'", 
            "','", "'?'", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "CLASS", "PUBLIC", "PRIVATE", "PROTECTED", "IF", "DO", "ELSE", 
            "RETURN", "BREAK", "WHILE", "FOR", "ENUM", "CONTINUE", "CASE", 
            "SWITCH", "STATIC", "FINAL", "ABSTRACT", "DEFAULT", "EXTENDS", 
            "IMPLEMENTS", "VOLATAILE", "THROWS", "TRY", "CATCH", "FINALLY", 
            "NEW", "THIS", "ASSERT", "IMPORT", "PACKAGE", "ADD", "PLUS", 
            "MINUS", "MULT", "DIV", "EQUAL", "ASSIGN", "NOT_EQUAL", "OR", 
            "AND", "MOD", "LESS", "GREATHER", "GREATHER_EQUAL", "LESS_EQUAL", 
            "LOGICAL_NOT", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
            "MOD_ASSIGN", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "SEMICOLON", 
            "LSQUARE", "RSQUARE", "INCREMENT", "DECREMENT", "SINGLE_LINE_COMMENT", 
            "MULTI_LINE_COMMENT", "NEWLINE", "TAB", "INTEGER", "INTEGER_TOKEN", 
            "FLOAT", "FLOAT_TOKEN", "VOID", "STRING", "STRING_TOKEN", "DOUBLE", 
            "LONG", "SHORT", "BYTE", "CHAR", "BOOLEAN", "INTEGERB", "DOUBLEB", 
            "FLOATB", "LONGB", "SHORTB", "BYTEB", "CHARACTERB", "BOOLEANB", 
            "ARRAY_LIST", "PRINT", "PRINTLN", "SCANNER", "NEXT", "IDENTIFIER", 
            "TRUE", "FALSE", "NULL", "INTEGER_NUMBER", "FLOAT_NUMBER", "DOT", 
            "COMMA", "TERNARY", "THE_DOUBLE_COLON", "WHITESPACE" ]

    ruleNames = [ "CLASS", "PUBLIC", "PRIVATE", "PROTECTED", "IF", "DO", 
                  "ELSE", "RETURN", "BREAK", "WHILE", "FOR", "ENUM", "CONTINUE", 
                  "CASE", "SWITCH", "STATIC", "FINAL", "ABSTRACT", "DEFAULT", 
                  "EXTENDS", "IMPLEMENTS", "VOLATAILE", "THROWS", "TRY", 
                  "CATCH", "FINALLY", "NEW", "THIS", "ASSERT", "IMPORT", 
                  "PACKAGE", "ADD", "PLUS", "MINUS", "MULT", "DIV", "EQUAL", 
                  "ASSIGN", "NOT_EQUAL", "OR", "AND", "MOD", "LESS", "GREATHER", 
                  "GREATHER_EQUAL", "LESS_EQUAL", "LOGICAL_NOT", "ADD_ASSIGN", 
                  "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                  "LPAREN", "RPAREN", "LBRACE", "RBRACE", "SEMICOLON", "LSQUARE", 
                  "RSQUARE", "INCREMENT", "DECREMENT", "SINGLE_LINE_COMMENT", 
                  "MULTI_LINE_COMMENT", "NEWLINE", "TAB", "INTEGER", "INTEGER_TOKEN", 
                  "FLOAT", "FLOAT_TOKEN", "VOID", "STRING", "STRING_TOKEN", 
                  "DOUBLE", "LONG", "SHORT", "BYTE", "CHAR", "BOOLEAN", 
                  "INTEGERB", "DOUBLEB", "FLOATB", "LONGB", "SHORTB", "BYTEB", 
                  "CHARACTERB", "BOOLEANB", "ARRAY_LIST", "PRINT", "PRINTLN", 
                  "SCANNER", "NEXT", "IDENTIFIER", "TRUE", "FALSE", "NULL", 
                  "DIGIT", "INTEGER_NUMBER", "FLOAT_NUMBER", "DOT", "COMMA", 
                  "TERNARY", "THE_DOUBLE_COLON", "WHITESPACE" ]

    grammarFileName = "java_babilon_lexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


