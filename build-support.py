#!/usr/bin/env python3
"""Build the Runlow support page in every language the app ships in.

The App Store lets each listing language carry its own support URL, so a German customer who
taps Support should not land on English (Leon, 2026-09-12: "you can make the support localized
too"). One template, one block of copy per language, and a strip at the top of every page so
anyone can switch. English stays at /support.html; the rest live at /support/<lang>.html.
"""
import pathlib

HERE = pathlib.Path(__file__).parent
LANGS = [("en", "English", "../support.html"), ("de", "Deutsch", "de.html"),
         ("fr", "Français", "fr.html"), ("es", "Español", "es.html"),
         ("it", "Italiano", "it.html"), ("nl", "Nederlands", "nl.html"),
         ("pt-BR", "Português", "pt-BR.html"), ("ja", "日本語", "ja.html"),
         ("zh-Hans", "简体中文", "zh-Hans.html"), ("ko", "한국어", "ko.html")]

CSS = """body{font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  max-width:720px;margin:40px auto;padding:0 20px;color:#1c1c1e;background:#fff}
h1{font-size:28px} h2{font-size:20px;margin-top:28px} a{color:#0a84ff}
.muted{color:#6b6b70;font-size:14px}
.langs{font-size:14px;margin-bottom:28px;color:#6b6b70}
.langs a{margin-right:10px;white-space:nowrap}
.langs strong{margin-right:10px;color:#1c1c1e}
@media(prefers-color-scheme:dark){body{background:#0e0e11;color:#e8e8ea}.muted,.langs{color:#9a9aa0}.langs strong{color:#e8e8ea}}"""

PAGE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
{css}
</style>
</head>
<body>
<p class="langs">{strip}</p>
<h1>{title}</h1>
{body}
<p class="muted">{disclaimer}</p>
</body>
</html>
"""


def strip_for(current, depth):
    out = []
    for code, label, href in LANGS:
        if depth == 0:                      # /support.html
            href = "support/" + href if code != "en" else "support.html"
        out.append(f"<strong>{label}</strong>" if code == current else f'<a href="{href}">{label}</a>')
    return "".join(out)


def write(code, title, body, disclaimer):
    depth = 0 if code == "en" else 1
    html = PAGE.format(lang=code, title=title, css=CSS, strip=strip_for(code, depth),
                       body=body.strip(), disclaimer=disclaimer)
    dest = HERE / "support.html" if code == "en" else HERE / "support" / f"{code}.html"
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    print(f"{code:8} {len(html):>6} bytes  {dest.relative_to(HERE)}")

EN_BODY = """
<p>Runlow shows how much of your AI usage you have left. It reads the limits for Claude, Codex (ChatGPT), Gemini CLI, Cursor, GitHub Copilot and OpenRouter and shows them as meters on your iPhone and iPad (dashboard, Lock Screen card, Dynamic Island and widgets), in your Mac's menu bar, on Apple Watch and on Apple Vision Pro.</p>
<p>Need help or found a bug? Email <a href="mailto:leonfigueira@gmail.com">leonfigueira@gmail.com</a>, or use <strong>Settings -&gt; Send feedback</strong> inside the app. Every message gets read.</p>

<h2>Getting started</h2>
<ul>
  <li><strong>Claude:</strong> paste your claude.ai session key. The app has a step-by-step guide showing exactly where to copy it from, and it checks the key before accepting it. Tip: sign in to claude.ai in a private window, copy the key, then close the window, so no open tab can sign it out later.</li>
  <li><strong>Codex (ChatGPT), Gemini CLI, Cursor, GitHub Copilot, OpenRouter:</strong> paste the token or API key from your own machine or account. The app shows you where each one lives.</li>
  <li><strong>On the Mac:</strong> Codex and Gemini can be read straight from their folders. Click Connect and grant access to <code>~/.codex</code> or <code>~/.gemini</code>.</li>
  <li><strong>Just looking?</strong> Turn on <em>Demo mode</em> to explore with sample data.</li>
  <li><strong>New here?</strong> The setup wizard walks you through the Lock Screen card one question at a time. It is in Settings whenever you want it again, and cancelling puts everything back.</li>
</ul>

<h2>Common questions</h2>
<p><strong>My meters stopped loading.</strong> Your session probably ended. Signing out of claude.ai in the browser you copied the key from, or "log out of all sessions" in Claude's settings, ends the key too, and Anthropic expires them on their own after a while. Runlow shows a banner with a Reconnect button when that happens. Paste a fresh key and everything else stays as it was. With sign-in sync on, your other devices pick up the new key on their next refresh. For the other services, paste the token again.</p>
<p><strong>The Lock Screen card looks out of date.</strong> Tap the refresh button on the card, or on a Home Screen widget. iOS decides when apps may run in the background, so the card refreshes when it can; the button asks for fresh numbers right now, and it will tell you if a refresh came back with nothing.</p>
<p><strong>I pasted a token and it says it was rejected.</strong> Check for a stray space or line break at the end of what you pasted. From 1.8.5 the app strips those itself.</p>
<p><strong>Do my settings follow me between devices?</strong> Yes, if you turn it on. Settings, then iCloud sync. Your sign-ins travel through your own iCloud Keychain (that part is on unless you turn it off); your colours, themes, meter names and Lock Screen layout travel through your own iCloud. From 1.8.7 your usage history can travel too, so a new or reset device picks up what your others recorded. Nothing goes through anyone else.</p>
<p><strong>Why can't I see the Gemini web-app limit?</strong> Google only exposes the Gemini CLI / Code Assist quota to apps; the gemini.google.com chat limit isn't readable outside the browser.</p>
<p><strong>Where's the Mac app?</strong> It lives in the menu bar. Look for the gauge icon at the top of your screen; it has no Dock icon. Click it for every meter, and right-click a meter to put it in the menu bar itself.</p>
<p><strong>Will updating change my setup?</strong> No. Themes, the wizard and every other option only change things when you use them.</p>

<h2>Privacy</h2>
<p>Runlow collects no data and has no server. The app's Privacy page (Settings, General, About, Privacy) lists every address it contacts and why. See the <a href="privacy.html">Privacy Policy</a>.</p>
"""

DE_BODY = """
<p>Runlow zeigt, wie viel von deiner KI-Nutzung noch übrig ist. Die App liest die Limits von Claude, Codex (ChatGPT), Gemini CLI, Cursor, GitHub Copilot und OpenRouter und zeigt sie als Anzeigen auf iPhone und iPad (Übersicht, Sperrbildschirm-Karte, Dynamic Island und Widgets), in der Menüleiste deines Macs, auf der Apple Watch und auf Apple Vision Pro.</p>
<p>Brauchst du Hilfe oder hast du einen Fehler gefunden? Schreib an <a href="mailto:leonfigueira@gmail.com">leonfigueira@gmail.com</a> oder nutze in der App <strong>Einstellungen → Feedback senden</strong>. Jede Nachricht wird gelesen.</p>

<h2>Erste Schritte</h2>
<ul>
  <li><strong>Claude:</strong> Füge deinen Sitzungsschlüssel von claude.ai ein. Die App führt dich Schritt für Schritt dorthin, wo du ihn kopierst, und prüft ihn, bevor sie ihn annimmt. Tipp: Melde dich in einem privaten Fenster bei claude.ai an, kopiere den Schlüssel und schließe das Fenster — dann kann kein offener Tab ihn später abmelden.</li>
  <li><strong>Codex (ChatGPT), Gemini CLI, Cursor, GitHub Copilot, OpenRouter:</strong> Füge das Token oder den API-Schlüssel von deinem eigenen Rechner oder Konto ein. Die App zeigt dir, wo jedes davon liegt.</li>
  <li><strong>Auf dem Mac:</strong> Codex und Gemini lassen sich direkt aus ihren Ordnern lesen. Klicke auf „Verbinden“ und erlaube den Zugriff auf <code>~/.codex</code> oder <code>~/.gemini</code>.</li>
  <li><strong>Erst mal schauen?</strong> Schalte den <em>Demomodus</em> ein und probiere alles mit Beispieldaten aus.</li>
  <li><strong>Neu hier?</strong> Der Einrichtungsassistent geht die Sperrbildschirm-Karte Frage für Frage mit dir durch. Er steht jederzeit in den Einstellungen, und „Abbrechen“ stellt alles zurück.</li>
</ul>

<h2>Häufige Fragen</h2>
<p><strong>Meine Anzeigen laden nicht mehr.</strong> Wahrscheinlich ist deine Sitzung beendet. Wenn du dich in dem Browser, aus dem du den Schlüssel kopiert hast, von claude.ai abmeldest — oder in Claudes Einstellungen „von allen Sitzungen abmelden“ wählst —, endet auch der Schlüssel; außerdem laufen sie bei Anthropic nach einer Weile von selbst ab. Runlow zeigt dann ein Banner mit „Neu verbinden“. Füge einen frischen Schlüssel ein, alles andere bleibt, wie es war. Ist die Anmeldung synchronisiert, übernehmen deine anderen Geräte den neuen Schlüssel bei ihrer nächsten Aktualisierung. Bei den anderen Diensten fügst du das Token erneut ein.</p>
<p><strong>Die Karte auf dem Sperrbildschirm wirkt veraltet.</strong> Tippe den Aktualisieren-Knopf auf der Karte oder auf einem Home-Bildschirm-Widget. iOS entscheidet, wann Apps im Hintergrund laufen dürfen; die Karte aktualisiert sich also, wenn sie darf. Der Knopf holt sofort frische Zahlen und sagt dir, wenn eine Aktualisierung nichts geliefert hat.</p>
<p><strong>Ich habe ein Token eingefügt und es wird abgelehnt.</strong> Prüfe, ob am Ende ein Leerzeichen oder ein Zeilenumbruch steht. Seit 1.8.5 entfernt die App beides selbst.</p>
<p><strong>Folgen mir meine Einstellungen zwischen den Geräten?</strong> Ja, wenn du es einschaltest: Einstellungen, dann iCloud-Sync. Deine Anmeldungen reisen über deinen eigenen iCloud-Schlüsselbund (das ist an, bis du es ausschaltest); Farben, Designs, Namen der Anzeigen und das Layout des Sperrbildschirms über deine eigene iCloud. Seit 1.8.7 kann auch dein Nutzungsverlauf mitreisen, sodass ein neues oder zurückgesetztes Gerät übernimmt, was deine anderen aufgezeichnet haben. Es läuft nichts über Dritte.</p>
<p><strong>Warum sehe ich das Limit der Gemini-Web-App nicht?</strong> Google gibt Apps nur das Kontingent von Gemini CLI / Code Assist preis; das Chat-Limit von gemini.google.com ist außerhalb des Browsers nicht lesbar.</p>
<p><strong>Wo ist die Mac-App?</strong> Sie lebt in der Menüleiste. Halte oben am Bildschirm nach dem Tacho-Symbol Ausschau; ein Dock-Symbol gibt es nicht. Ein Klick zeigt jede Anzeige, und mit einem Rechtsklick legst du eine Anzeige in die Menüleiste selbst.</p>
<p><strong>Ändert ein Update meine Einrichtung?</strong> Nein. Designs, der Assistent und jede andere Option ändern nur dann etwas, wenn du sie benutzt.</p>

<h2>Datenschutz</h2>
<p>Runlow erhebt keine Daten und hat keinen Server. Die Datenschutzseite in der App (Einstellungen → Allgemein → Über die App → Datenschutz) listet jede Adresse auf, die kontaktiert wird, und warum. Siehe die <a href="../privacy.html">Datenschutzerklärung</a>.</p>
"""


FR_BODY = """
<p>Runlow montre ce qu’il vous reste de votre consommation d’IA. L’app lit les limites de Claude, Codex (ChatGPT), Gemini CLI, Cursor, GitHub Copilot et OpenRouter et les affiche sous forme de jauges sur votre iPhone et votre iPad (tableau de bord, carte d’écran verrouillé, Dynamic Island et widgets), dans la barre des menus de votre Mac, sur l’Apple Watch et sur l’Apple Vision Pro.</p>
<p>Besoin d’aide ou vous avez trouvé un bug ? Écrivez à <a href="mailto:leonfigueira@gmail.com">leonfigueira@gmail.com</a>, ou utilisez <strong>Réglages → Envoyer un retour</strong> dans l’app. Chaque message est lu.</p>

<h2>Pour commencer</h2>
<ul>
  <li><strong>Claude :</strong> collez votre clé de session claude.ai. L’app vous montre pas à pas où la copier, et la vérifie avant de l’accepter. Astuce : connectez-vous à claude.ai dans une fenêtre privée, copiez la clé, puis fermez la fenêtre — ainsi aucun onglet ouvert ne pourra la déconnecter plus tard.</li>
  <li><strong>Codex (ChatGPT), Gemini CLI, Cursor, GitHub Copilot, OpenRouter :</strong> collez le jeton ou la clé d’API depuis votre propre machine ou votre compte. L’app vous indique où se trouve chacun.</li>
  <li><strong>Sur le Mac :</strong> Codex et Gemini se lisent directement depuis leurs dossiers. Cliquez sur Connecter et accordez l’accès à <code>~/.codex</code> ou <code>~/.gemini</code>.</li>
  <li><strong>Juste un coup d’œil ?</strong> Activez le <em>mode démo</em> pour explorer avec des données d’exemple.</li>
  <li><strong>Nouveau ?</strong> L’assistant de configuration vous guide dans la carte de l’écran verrouillé, une question à la fois. Il reste dans les Réglages, et Annuler remet tout en place.</li>
</ul>

<h2>Questions fréquentes</h2>
<p><strong>Mes jauges ne se chargent plus.</strong> Votre session s’est probablement terminée. Vous déconnecter de claude.ai dans le navigateur d’où vous avez copié la clé, ou choisir « déconnecter toutes les sessions » dans les réglages de Claude, met fin à la clé ; et Anthropic les fait expirer d’elles-mêmes au bout d’un moment. Runlow affiche alors une bannière avec un bouton Reconnecter. Collez une clé fraîche et tout le reste demeure. Si la synchronisation de la connexion est activée, vos autres appareils reprennent la nouvelle clé à leur prochaine actualisation. Pour les autres services, recollez le jeton.</p>
<p><strong>La carte de l’écran verrouillé semble dépassée.</strong> Touchez le bouton d’actualisation sur la carte, ou sur un widget de l’écran d’accueil. iOS décide quand une app peut s’exécuter en arrière-plan : la carte se met à jour quand elle le peut, et le bouton demande des chiffres frais tout de suite — il vous dira si l’actualisation n’a rien rapporté.</p>
<p><strong>J’ai collé un jeton et il est refusé.</strong> Vérifiez qu’il n’y a pas d’espace ou de retour à la ligne à la fin. Depuis la 1.8.5, l’app les retire elle-même.</p>
<p><strong>Mes réglages me suivent-ils d’un appareil à l’autre ?</strong> Oui, si vous l’activez : Réglages, puis Synchronisation iCloud. Vos connexions passent par votre propre trousseau iCloud (activé tant que vous ne le désactivez pas) ; vos couleurs, thèmes, noms de jauges et la disposition de l’écran verrouillé passent par votre propre iCloud. Depuis la 1.8.7, votre historique d’utilisation peut voyager aussi, si bien qu’un appareil neuf ou réinitialisé récupère ce que les autres ont enregistré. Rien ne transite par un tiers.</p>
<p><strong>Pourquoi ne puis-je pas voir la limite de l’app web Gemini ?</strong> Google n’expose aux apps que le quota Gemini CLI / Code Assist ; la limite de conversation de gemini.google.com n’est pas lisible hors du navigateur.</p>
<p><strong>Où est l’app Mac ?</strong> Elle vit dans la barre des menus. Cherchez l’icône de jauge en haut de l’écran ; il n’y a pas d’icône dans le Dock. Un clic affiche toutes les jauges, et un clic droit place une jauge dans la barre des menus elle-même.</p>
<p><strong>Une mise à jour va-t-elle changer ma configuration ?</strong> Non. Les thèmes, l’assistant et toutes les autres options ne changent quelque chose que lorsque vous vous en servez.</p>

<h2>Confidentialité</h2>
<p>Runlow ne collecte aucune donnée et n’a pas de serveur. La page Confidentialité de l’app (Réglages, Général, À propos, Confidentialité) liste chaque adresse contactée et pourquoi. Voir la <a href="../privacy.html">politique de confidentialité</a>.</p>
"""

ES_BODY = """
<p>Runlow muestra cuánto te queda de tu uso de IA. La app lee los límites de Claude, Codex (ChatGPT), Gemini CLI, Cursor, GitHub Copilot y OpenRouter y los muestra como medidores en tu iPhone y iPad (panel, tarjeta de la pantalla de bloqueo, Dynamic Island y widgets), en la barra de menús del Mac, en el Apple Watch y en el Apple Vision Pro.</p>
<p>¿Necesitas ayuda o has encontrado un fallo? Escribe a <a href="mailto:leonfigueira@gmail.com">leonfigueira@gmail.com</a>, o usa <strong>Ajustes → Enviar comentarios</strong> dentro de la app. Todos los mensajes se leen.</p>

<h2>Para empezar</h2>
<ul>
  <li><strong>Claude:</strong> pega tu clave de sesión de claude.ai. La app te guía paso a paso hasta dónde copiarla y la comprueba antes de aceptarla. Consejo: inicia sesión en claude.ai en una ventana privada, copia la clave y cierra la ventana; así ninguna pestaña abierta podrá cerrarla más tarde.</li>
  <li><strong>Codex (ChatGPT), Gemini CLI, Cursor, GitHub Copilot, OpenRouter:</strong> pega el token o la clave de API desde tu propio equipo o cuenta. La app te enseña dónde está cada uno.</li>
  <li><strong>En el Mac:</strong> Codex y Gemini se leen directamente de sus carpetas. Haz clic en Conectar y concede acceso a <code>~/.codex</code> o <code>~/.gemini</code>.</li>
  <li><strong>¿Solo mirando?</strong> Activa el <em>modo demo</em> para explorar con datos de ejemplo.</li>
  <li><strong>¿Nuevo por aquí?</strong> El asistente de configuración te lleva por la tarjeta de la pantalla de bloqueo una pregunta cada vez. Está en Ajustes cuando quieras, y Cancelar lo devuelve todo.</li>
</ul>

<h2>Preguntas frecuentes</h2>
<p><strong>Mis medidores han dejado de cargar.</strong> Seguramente terminó tu sesión. Cerrar sesión en claude.ai en el navegador desde el que copiaste la clave, o usar «cerrar todas las sesiones» en los ajustes de Claude, también acaba con la clave; además, Anthropic las caduca por su cuenta al cabo de un tiempo. Runlow muestra entonces un aviso con un botón Reconectar. Pega una clave nueva y todo lo demás sigue igual. Con la sincronización de la sesión activada, tus otros dispositivos toman la clave nueva en su próxima actualización. Para los demás servicios, vuelve a pegar el token.</p>
<p><strong>La tarjeta de la pantalla de bloqueo parece desactualizada.</strong> Toca el botón de actualizar en la tarjeta o en un widget de la pantalla de inicio. iOS decide cuándo puede ejecutarse una app en segundo plano, así que la tarjeta se actualiza cuando puede; el botón pide cifras frescas al instante y te dirá si la actualización no trajo nada.</p>
<p><strong>He pegado un token y dice que lo rechaza.</strong> Comprueba si hay un espacio o un salto de línea al final. Desde la 1.8.5 la app los quita sola.</p>
<p><strong>¿Mis ajustes me siguen entre dispositivos?</strong> Sí, si lo activas: Ajustes y luego Sincronización de iCloud. Tus inicios de sesión viajan por tu propio llavero de iCloud (esto está activado salvo que lo desactives); tus colores, temas, nombres de medidores y la disposición de la pantalla de bloqueo, por tu propio iCloud. Desde la 1.8.7 tu historial de uso también puede viajar, así que un dispositivo nuevo o restablecido recoge lo que registraron los demás. Nada pasa por terceros.</p>
<p><strong>¿Por qué no veo el límite de la web de Gemini?</strong> Google solo expone a las apps la cuota de Gemini CLI / Code Assist; el límite del chat de gemini.google.com no se puede leer fuera del navegador.</p>
<p><strong>¿Dónde está la app del Mac?</strong> Vive en la barra de menús. Busca el icono del medidor en la parte superior de la pantalla; no tiene icono en el Dock. Haz clic para ver todos los medidores, y clic derecho en uno para ponerlo en la propia barra de menús.</p>
<p><strong>¿Actualizar cambiará mi configuración?</strong> No. Los temas, el asistente y cualquier otra opción solo cambian algo cuando los usas.</p>

<h2>Privacidad</h2>
<p>Runlow no recopila datos y no tiene servidor. La página de Privacidad de la app (Ajustes, General, Acerca de, Privacidad) enumera cada dirección que contacta y por qué. Consulta la <a href="../privacy.html">política de privacidad</a>.</p>
"""

IT_BODY = """
<p>Runlow mostra quanto ti resta del tuo utilizzo di IA. L’app legge i limiti di Claude, Codex (ChatGPT), Gemini CLI, Cursor, GitHub Copilot e OpenRouter e li mostra come indicatori su iPhone e iPad (pannello, scheda della schermata di blocco, Dynamic Island e widget), nella barra dei menu del Mac, su Apple Watch e su Apple Vision Pro.</p>
<p>Ti serve aiuto o hai trovato un problema? Scrivi a <a href="mailto:leonfigueira@gmail.com">leonfigueira@gmail.com</a>, oppure usa <strong>Impostazioni → Invia un riscontro</strong> nell’app. Ogni messaggio viene letto.</p>

<h2>Per iniziare</h2>
<ul>
  <li><strong>Claude:</strong> incolla la tua chiave di sessione di claude.ai. L’app ti mostra passo passo dove copiarla e la verifica prima di accettarla. Consiglio: accedi a claude.ai in una finestra privata, copia la chiave e chiudi la finestra — così nessuna scheda aperta potrà disconnetterla in seguito.</li>
  <li><strong>Codex (ChatGPT), Gemini CLI, Cursor, GitHub Copilot, OpenRouter:</strong> incolla il token o la chiave API dal tuo computer o dal tuo account. L’app ti indica dove si trova ciascuno.</li>
  <li><strong>Sul Mac:</strong> Codex e Gemini si leggono direttamente dalle loro cartelle. Fai clic su Collega e concedi l’accesso a <code>~/.codex</code> o <code>~/.gemini</code>.</li>
  <li><strong>Solo un’occhiata?</strong> Attiva la <em>modalità demo</em> per esplorare con dati di esempio.</li>
  <li><strong>Sei nuovo?</strong> La configurazione guidata ti accompagna nella scheda della schermata di blocco una domanda alla volta. Resta nelle Impostazioni quando vuoi, e Annulla rimette tutto a posto.</li>
</ul>

<h2>Domande frequenti</h2>
<p><strong>I miei indicatori non si caricano più.</strong> Probabilmente la sessione è finita. Uscire da claude.ai nel browser da cui hai copiato la chiave, o scegliere «esci da tutte le sessioni» nelle impostazioni di Claude, chiude anche la chiave; inoltre Anthropic le fa scadere da sole dopo un po’. Runlow mostra allora un avviso con un pulsante Ricollega. Incolla una chiave nuova e tutto il resto resta com’era. Con la sincronizzazione dell’accesso attiva, gli altri tuoi dispositivi prendono la nuova chiave al prossimo aggiornamento. Per gli altri servizi, incolla di nuovo il token.</p>
<p><strong>La scheda sulla schermata di blocco sembra vecchia.</strong> Tocca il pulsante di aggiornamento sulla scheda, o su un widget della schermata Home. È iOS a decidere quando un’app può girare in background, quindi la scheda si aggiorna quando può; il pulsante chiede numeri freschi subito e ti dice se un aggiornamento non ha portato nulla.</p>
<p><strong>Ho incollato un token e viene rifiutato.</strong> Controlla che alla fine non ci sia uno spazio o un a capo. Dalla 1.8.5 l’app li toglie da sola.</p>
<p><strong>Le mie impostazioni mi seguono tra i dispositivi?</strong> Sì, se lo attivi: Impostazioni, poi Sincronizzazione iCloud. I tuoi accessi viaggiano nel tuo portachiavi iCloud (attivo finché non lo disattivi); colori, temi, nomi degli indicatori e la disposizione della schermata di blocco nel tuo iCloud. Dalla 1.8.7 può viaggiare anche la cronologia di utilizzo, così un dispositivo nuovo o ripristinato riprende quello che gli altri hanno registrato. Non passa nulla da terzi.</p>
<p><strong>Perché non vedo il limite dell’app web di Gemini?</strong> Google espone alle app solo la quota di Gemini CLI / Code Assist; il limite della chat su gemini.google.com non è leggibile fuori dal browser.</p>
<p><strong>Dov’è l’app per Mac?</strong> Vive nella barra dei menu. Cerca l’icona dell’indicatore in cima allo schermo; non ha icona nel Dock. Un clic mostra tutti gli indicatori, e un clic destro ne mette uno nella barra dei menu stessa.</p>
<p><strong>Aggiornare cambierà la mia configurazione?</strong> No. I temi, la configurazione guidata e ogni altra opzione cambiano qualcosa solo quando le usi.</p>

<h2>Privacy</h2>
<p>Runlow non raccoglie dati e non ha server. La pagina Privacy nell’app (Impostazioni, Generali, Info, Privacy) elenca ogni indirizzo contattato e perché. Vedi l’<a href="../privacy.html">informativa sulla privacy</a>.</p>
"""

NL_BODY = """
<p>Runlow laat zien hoeveel van je AI-gebruik je nog over hebt. De app leest de limieten van Claude, Codex (ChatGPT), Gemini CLI, Cursor, GitHub Copilot en OpenRouter en toont ze als meters op je iPhone en iPad (dashboard, kaart op het toegangsscherm, Dynamic Island en widgets), in de menubalk van je Mac, op de Apple Watch en op de Apple Vision Pro.</p>
<p>Hulp nodig of een fout gevonden? Mail <a href="mailto:leonfigueira@gmail.com">leonfigueira@gmail.com</a>, of gebruik <strong>Instellingen → Stuur feedback</strong> in de app. Elk bericht wordt gelezen.</p>

<h2>Aan de slag</h2>
<ul>
  <li><strong>Claude:</strong> plak je sessiesleutel van claude.ai. De app laat stap voor stap zien waar je hem kopieert en controleert hem voordat hij wordt geaccepteerd. Tip: log in bij claude.ai in een privévenster, kopieer de sleutel en sluit het venster — dan kan geen enkel open tabblad hem later uitloggen.</li>
  <li><strong>Codex (ChatGPT), Gemini CLI, Cursor, GitHub Copilot, OpenRouter:</strong> plak het token of de API-sleutel van je eigen machine of account. De app laat zien waar je ze vindt.</li>
  <li><strong>Op de Mac:</strong> Codex en Gemini kunnen rechtstreeks uit hun mappen worden gelezen. Klik op Koppel en geef toegang tot <code>~/.codex</code> of <code>~/.gemini</code>.</li>
  <li><strong>Even kijken?</strong> Zet de <em>demomodus</em> aan en verken alles met voorbeeldgegevens.</li>
  <li><strong>Nieuw hier?</strong> De configuratieassistent loopt de kaart op het toegangsscherm met je door, één vraag tegelijk. Hij staat altijd in Instellingen, en Annuleren zet alles terug.</li>
</ul>

<h2>Veelgestelde vragen</h2>
<p><strong>Mijn meters laden niet meer.</strong> Waarschijnlijk is je sessie beëindigd. Uitloggen bij claude.ai in de browser waaruit je de sleutel kopieerde, of 'uitloggen op alle sessies' in de instellingen van Claude, beëindigt de sleutel ook; bovendien laat Anthropic ze na verloop van tijd vanzelf verlopen. Runlow toont dan een banner met een knop Koppel opnieuw. Plak een nieuwe sleutel en al het andere blijft zoals het was. Staat het synchroniseren van het inloggen aan, dan nemen je andere apparaten de nieuwe sleutel over bij hun volgende verversing. Voor de andere diensten plak je het token opnieuw.</p>
<p><strong>De kaart op het toegangsscherm lijkt verouderd.</strong> Tik op de verversknop op de kaart, of op een widget op het beginscherm. iOS bepaalt wanneer apps op de achtergrond mogen draaien, dus de kaart ververst wanneer het mag; de knop vraagt nu meteen om verse cijfers en zegt het als een verversing niets opleverde.</p>
<p><strong>Ik heb een token geplakt en het wordt geweigerd.</strong> Kijk of er een spatie of regeleinde aan het eind staat. Sinds 1.8.5 haalt de app die er zelf af.</p>
<p><strong>Reizen mijn instellingen mee tussen apparaten?</strong> Ja, als je het aanzet: Instellingen, dan iCloud-synchronisatie. Je logins reizen via je eigen iCloud-sleutelhanger (dat staat aan tot je het uitzet); je kleuren, thema's, meternamen en de indeling van het toegangsscherm via je eigen iCloud. Sinds 1.8.7 kan ook je gebruiksgeschiedenis meereizen, zodat een nieuw of gewist apparaat oppikt wat je andere hebben vastgelegd. Er gaat niets langs derden.</p>
<p><strong>Waarom zie ik de limiet van de Gemini-webapp niet?</strong> Google geeft apps alleen het quotum van Gemini CLI / Code Assist; de chatlimiet van gemini.google.com is buiten de browser niet leesbaar.</p>
<p><strong>Waar is de Mac-app?</strong> Die woont in de menubalk. Zoek het metersymbool bovenaan je scherm; er is geen Dock-symbool. Eén klik toont elke meter, en met een rechtermuisklik zet je een meter in de menubalk zelf.</p>
<p><strong>Verandert bijwerken mijn instellingen?</strong> Nee. Thema's, de assistent en elke andere optie veranderen pas iets wanneer je ze gebruikt.</p>

<h2>Privacy</h2>
<p>Runlow verzamelt geen gegevens en heeft geen server. De privacypagina in de app (Instellingen, Algemeen, Info, Privacy) noemt elk adres dat wordt benaderd en waarom. Zie het <a href="../privacy.html">privacybeleid</a>.</p>
"""


PT_BODY = """
<p>O Runlow mostra quanto sobrou do seu uso de IA. O app lê os limites de Claude, Codex (ChatGPT), Gemini CLI, Cursor, GitHub Copilot e OpenRouter e os mostra como medidores no seu iPhone e iPad (painel, cartão da Tela Bloqueada, Dynamic Island e widgets), na barra de menus do Mac, no Apple Watch e no Apple Vision Pro.</p>
<p>Precisa de ajuda ou encontrou um erro? Escreva para <a href="mailto:leonfigueira@gmail.com">leonfigueira@gmail.com</a>, ou use <strong>Ajustes → Enviar feedback</strong> dentro do app. Toda mensagem é lida.</p>

<h2>Primeiros passos</h2>
<ul>
  <li><strong>Claude:</strong> cole sua chave de sessão do claude.ai. O app mostra passo a passo onde copiá-la e a verifica antes de aceitar. Dica: entre no claude.ai em uma janela privada, copie a chave e feche a janela — assim nenhuma aba aberta poderá encerrá-la depois.</li>
  <li><strong>Codex (ChatGPT), Gemini CLI, Cursor, GitHub Copilot, OpenRouter:</strong> cole o token ou a chave de API da sua própria máquina ou conta. O app mostra onde cada um fica.</li>
  <li><strong>No Mac:</strong> Codex e Gemini podem ser lidos direto das pastas deles. Clique em Conectar e conceda acesso a <code>~/.codex</code> ou <code>~/.gemini</code>.</li>
  <li><strong>Só dando uma olhada?</strong> Ative o <em>modo demo</em> para explorar com dados de exemplo.</li>
  <li><strong>Novo por aqui?</strong> O assistente de configuração percorre o cartão da Tela Bloqueada com você, uma pergunta por vez. Ele fica nos Ajustes sempre que quiser, e Cancelar devolve tudo.</li>
</ul>

<h2>Perguntas frequentes</h2>
<p><strong>Meus medidores pararam de carregar.</strong> Provavelmente sua sessão terminou. Sair do claude.ai no navegador de onde você copiou a chave, ou usar "sair de todas as sessões" nos ajustes do Claude, também encerra a chave; além disso, a Anthropic faz elas expirarem sozinhas depois de um tempo. O Runlow mostra então um aviso com um botão Reconectar. Cole uma chave nova e todo o resto continua igual. Com a sincronização do login ligada, seus outros aparelhos pegam a chave nova na próxima atualização. Para os outros serviços, cole o token de novo.</p>
<p><strong>O cartão da Tela Bloqueada parece desatualizado.</strong> Toque no botão de atualizar no cartão, ou em um widget da Tela de Início. O iOS decide quando um app pode rodar em segundo plano, então o cartão atualiza quando pode; o botão pede números novos na hora e avisa se a atualização não trouxe nada.</p>
<p><strong>Colei um token e ele foi recusado.</strong> Veja se há um espaço ou uma quebra de linha no fim. Desde a 1.8.5 o app tira isso sozinho.</p>
<p><strong>Meus ajustes me acompanham entre aparelhos?</strong> Sim, se você ligar: Ajustes e depois Sincronização do iCloud. Seus logins viajam pelas suas próprias Chaves do iCloud (isso fica ligado até você desligar); suas cores, temas, nomes de medidores e a disposição da Tela Bloqueada, pelo seu próprio iCloud. Desde a 1.8.7 seu histórico de uso também pode viajar, então um aparelho novo ou restaurado recupera o que os outros registraram. Nada passa por terceiros.</p>
<p><strong>Por que não vejo o limite do app web do Gemini?</strong> O Google só expõe aos apps a cota do Gemini CLI / Code Assist; o limite do chat em gemini.google.com não pode ser lido fora do navegador.</p>
<p><strong>Onde está o app do Mac?</strong> Ele mora na barra de menus. Procure o ícone do medidor no topo da tela; não há ícone no Dock. Clique para ver todos os medidores, e clique com o botão direito em um deles para colocá-lo na própria barra de menus.</p>
<p><strong>Atualizar vai mudar minha configuração?</strong> Não. Temas, o assistente e qualquer outra opção só mudam algo quando você os usa.</p>

<h2>Privacidade</h2>
<p>O Runlow não coleta dados e não tem servidor. A página de Privacidade do app (Ajustes, Geral, Sobre, Privacidade) lista cada endereço que ele contata e por quê. Veja a <a href="../privacy.html">política de privacidade</a>.</p>
"""

JA_BODY = """
<p>Runlowは、AIの使用量があとどれだけ残っているかを表示します。Claude、Codex（ChatGPT）、Gemini CLI、Cursor、GitHub Copilot、OpenRouterの上限を読み取り、iPhoneとiPad（ダッシュボード、ロック画面のカード、Dynamic Island、ウィジェット）、Macのメニューバー、Apple Watch、Apple Vision Proにメーターとして表示します。</p>
<p>お困りですか。不具合を見つけましたか。<a href="mailto:leonfigueira@gmail.com">leonfigueira@gmail.com</a> までメールいただくか、アプリ内の<strong>「設定」→「フィードバックを送る」</strong>をお使いください。いただいたメッセージはすべて読んでいます。</p>

<h2>はじめかた</h2>
<ul>
  <li><strong>Claude：</strong>claude.aiのセッションキーを貼り付けます。どこからコピーするかはアプリが順を追って案内し、受け入れる前にキーを確認します。コツ：プライベートウィンドウでclaude.aiにログインし、キーをコピーしてからウィンドウを閉じてください。開いたタブが後からキーを無効にすることがなくなります。</li>
  <li><strong>Codex（ChatGPT）、Gemini CLI、Cursor、GitHub Copilot、OpenRouter：</strong>ご自身のマシンやアカウントからトークンまたはAPIキーを貼り付けます。それぞれの場所はアプリが案内します。</li>
  <li><strong>Macでは：</strong>CodexとGeminiはフォルダから直接読み取れます。「接続」をクリックし、<code>~/.codex</code> または <code>~/.gemini</code> へのアクセスを許可してください。</li>
  <li><strong>まず見てみたい：</strong><em>デモモード</em>をオンにすると、サンプルデータで試せます。</li>
  <li><strong>はじめての方へ：</strong>設定ガイドが、ロック画面のカードを一問ずつ案内します。設定からいつでも呼び出せ、「キャンセル」ですべて元に戻ります。</li>
</ul>

<h2>よくある質問</h2>
<p><strong>メーターが読み込まれなくなりました。</strong>おそらくセッションが終了しています。キーをコピーしたブラウザでclaude.aiからログアウトしたり、Claudeの設定で「すべてのセッションからログアウト」を選んだりすると、キーも終了します。またAnthropic側でも、しばらくすると自動的に期限切れになります。その場合Runlowは「再接続」ボタン付きのバナーを表示します。新しいキーを貼り付ければ、ほかの設定はそのままです。ログインの同期がオンなら、ほかの端末も次の更新時に新しいキーを受け取ります。ほかのサービスでは、トークンを貼り直してください。</p>
<p><strong>ロック画面のカードが古いままに見えます。</strong>カード上、またはホーム画面ウィジェットの更新ボタンをタップしてください。アプリがバックグラウンドで動けるタイミングはiOSが決めるため、カードは可能なときに更新されます。ボタンを押せばその場で最新の数字を取りに行き、何も取得できなかった場合はその旨をお伝えします。</p>
<p><strong>トークンを貼り付けたのに拒否されます。</strong>末尾に余分な空白や改行が入っていないか確認してください。1.8.5からはアプリ側で取り除きます。</p>
<p><strong>設定は端末間で引き継がれますか。</strong>オンにすればはい。「設定」→「iCloud同期」です。ログインはご自身のiCloudキーチェーンを（こちらはオフにしない限りオンです）、色・テーマ・メーター名・ロック画面のレイアウトはご自身のiCloudを通ります。1.8.7からは使用量の履歴も引き継げるので、新しい端末や初期化した端末が、ほかの端末の記録を受け取れます。第三者を経由するものはありません。</p>
<p><strong>Geminiのウェブ版の上限が見えないのはなぜですか。</strong>Googleがアプリに公開しているのはGemini CLI / Code Assistのクォータだけで、gemini.google.comのチャットの上限はブラウザの外からは読めません。</p>
<p><strong>Macアプリはどこにありますか。</strong>メニューバーにいます。画面上部のゲージのアイコンを探してください。Dockにアイコンは出ません。クリックすればすべてのメーターが開き、メーターを右クリックするとメニューバー自体に並べられます。</p>
<p><strong>アップデートで設定は変わりますか。</strong>いいえ。テーマも設定ガイドもそのほかの項目も、あなたが操作したときにだけ変わります。</p>

<h2>プライバシー</h2>
<p>Runlowはデータを収集せず、サーバーも持ちません。アプリ内のプライバシーページ（設定 → 一般 → このアプリについて → プライバシー）に、接続先のアドレスとその理由がすべて記載されています。<a href="../privacy.html">プライバシーポリシー</a>もご覧ください。</p>
"""

ZH_BODY = """
<p>Runlow 显示你的 AI 用量还剩多少。它读取 Claude、Codex（ChatGPT）、Gemini CLI、Cursor、GitHub Copilot 和 OpenRouter 的额度，并在 iPhone 和 iPad（面板、锁屏卡片、Dynamic Island 和小组件）、Mac 菜单栏、Apple Watch 以及 Apple Vision Pro 上以用量条的形式呈现。</p>
<p>需要帮助，或者发现了问题？请发邮件到 <a href="mailto:leonfigueira@gmail.com">leonfigueira@gmail.com</a>，或在 App 内使用<strong>「设置 → 发送反馈」</strong>。每一封都会被看到。</p>

<h2>开始使用</h2>
<ul>
  <li><strong>Claude：</strong>粘贴你的 claude.ai 会话密钥。App 会一步步告诉你从哪里复制，并在接受之前先做校验。小技巧：在隐私窗口登录 claude.ai，复制密钥后关掉窗口，这样就不会有打开的标签页在之后把它注销。</li>
  <li><strong>Codex（ChatGPT）、Gemini CLI、Cursor、GitHub Copilot、OpenRouter：</strong>从你自己的电脑或账户里粘贴令牌或 API 密钥。App 会告诉你每一个在哪里。</li>
  <li><strong>在 Mac 上：</strong>Codex 和 Gemini 可以直接从各自的文件夹读取。点击「连接」并授予对 <code>~/.codex</code> 或 <code>~/.gemini</code> 的访问权限。</li>
  <li><strong>只是看看？</strong>打开<em>演示模式</em>，用示例数据随便逛。</li>
  <li><strong>第一次用？</strong>设置向导会一次一个问题地带你配置锁屏卡片。它随时在「设置」里，点「取消」则一切还原。</li>
</ul>

<h2>常见问题</h2>
<p><strong>用量条不再加载了。</strong>多半是会话已经结束。在你复制密钥的那个浏览器里退出 claude.ai，或者在 Claude 的设置中选择「退出所有会话」，都会让密钥一并失效；另外 Anthropic 也会在一段时间后让它自动过期。这时 Runlow 会显示一条带「重新连接」按钮的提示。粘贴一个新密钥即可，其他设置照旧。打开同步登录后，你的其他设备会在下次刷新时自动用上新密钥。其他服务则重新粘贴令牌。</p>
<p><strong>锁屏卡片看起来是旧的。</strong>点一下卡片上的刷新按钮，或主屏幕小组件上的那个。App 什么时候能在后台运行由 iOS 决定，所以卡片会在允许时更新；而这个按钮会立刻去取新数据，如果这次刷新什么也没拿到，它也会告诉你。</p>
<p><strong>我粘贴了令牌，却提示被拒绝。</strong>检查末尾是否多了空格或换行。从 1.8.5 起，App 会自己去掉它们。</p>
<p><strong>我的设置会在设备之间同步吗？</strong>会，只要你打开它：「设置 → iCloud 同步」。登录信息通过你自己的 iCloud 钥匙串（这一项默认开启，除非你关掉），颜色、主题、用量条名称和锁屏布局通过你自己的 iCloud。从 1.8.7 起，用量历史也能一起同步，新设备或重置过的设备可以拿回其他设备记录的内容。不会经过任何第三方。</p>
<p><strong>为什么看不到 Gemini 网页版的额度？</strong>Google 只向 App 开放 Gemini CLI / Code Assist 的配额；gemini.google.com 的聊天额度在浏览器之外无法读取。</p>
<p><strong>Mac App 在哪里？</strong>它在菜单栏里。看看屏幕顶部那个仪表图标；它没有 Dock 图标。点一下可以看到全部用量条，右键点按某个用量条还能把它放进菜单栏本身。</p>
<p><strong>更新会改变我的配置吗？</strong>不会。主题、向导和其他所有选项，只有你动它们时才会改变什么。</p>

<h2>隐私</h2>
<p>Runlow 不收集数据，也没有服务器。App 内的隐私页面（设置 → 通用 → 关于 → 隐私）列出了它联系的每一个地址以及原因。另见<a href="../privacy.html">隐私政策</a>。</p>
"""

KO_BODY = """
<p>Runlow는 AI 사용량이 얼마나 남았는지 보여줍니다. Claude, Codex(ChatGPT), Gemini CLI, Cursor, GitHub Copilot, OpenRouter의 한도를 읽어 iPhone과 iPad(대시보드, 잠금 화면 카드, Dynamic Island, 위젯), Mac의 메뉴 막대, Apple Watch, Apple Vision Pro에 미터로 표시합니다.</p>
<p>도움이 필요하거나 문제를 발견하셨나요? <a href="mailto:leonfigueira@gmail.com">leonfigueira@gmail.com</a>으로 메일을 보내시거나, 앱에서 <strong>설정 → 의견 보내기</strong>를 이용해 주세요. 모든 메시지를 읽고 있습니다.</p>

<h2>시작하기</h2>
<ul>
  <li><strong>Claude:</strong> claude.ai 세션 키를 붙여넣으세요. 어디에서 복사하는지 앱이 단계별로 안내하고, 받아들이기 전에 키를 확인합니다. 팁: 시크릿 창에서 claude.ai에 로그인해 키를 복사한 뒤 창을 닫으세요. 열린 탭이 나중에 키를 로그아웃시킬 일이 없어집니다.</li>
  <li><strong>Codex(ChatGPT), Gemini CLI, Cursor, GitHub Copilot, OpenRouter:</strong> 본인의 컴퓨터나 계정에서 토큰 또는 API 키를 붙여넣으세요. 각각 어디에 있는지 앱이 알려줍니다.</li>
  <li><strong>Mac에서는:</strong> Codex와 Gemini는 각자의 폴더에서 바로 읽을 수 있습니다. '연결'을 클릭하고 <code>~/.codex</code> 또는 <code>~/.gemini</code>에 접근을 허용해 주세요.</li>
  <li><strong>둘러보는 중이신가요?</strong> <em>데모 모드</em>를 켜면 예시 데이터로 살펴볼 수 있습니다.</li>
  <li><strong>처음이신가요?</strong> 설정 마법사가 잠금 화면 카드를 한 번에 한 가지씩 안내합니다. 언제든 설정에서 다시 열 수 있고, 취소하면 모두 원래대로 돌아갑니다.</li>
</ul>

<h2>자주 묻는 질문</h2>
<p><strong>미터가 더 이상 불러와지지 않습니다.</strong> 세션이 끝났을 가능성이 큽니다. 키를 복사한 브라우저에서 claude.ai를 로그아웃하거나 Claude 설정에서 '모든 세션에서 로그아웃'을 고르면 키도 함께 끝나고, Anthropic 쪽에서도 일정 시간이 지나면 스스로 만료시킵니다. 그럴 때 Runlow는 '다시 연결' 버튼이 있는 배너를 보여줍니다. 새 키를 붙여넣으면 나머지는 그대로 유지됩니다. 로그인 동기화가 켜져 있으면 다른 기기도 다음 새로고침 때 새 키를 받아 옵니다. 다른 서비스는 토큰을 다시 붙여넣으세요.</p>
<p><strong>잠금 화면 카드가 오래된 것처럼 보입니다.</strong> 카드나 홈 화면 위젯의 새로고침 버튼을 누르세요. 앱이 백그라운드에서 언제 실행될 수 있는지는 iOS가 정하므로 카드는 가능할 때 갱신됩니다. 버튼을 누르면 지금 바로 새 수치를 가져오고, 아무것도 받지 못했다면 그 사실도 알려줍니다.</p>
<p><strong>토큰을 붙여넣었는데 거부된다고 나옵니다.</strong> 끝에 공백이나 줄바꿈이 섞이지 않았는지 확인해 보세요. 1.8.5부터는 앱이 알아서 지워 줍니다.</p>
<p><strong>설정이 기기 사이를 따라오나요?</strong> 켜 두면 그렇습니다. 설정에서 iCloud 동기화를 여세요. 로그인은 본인의 iCloud 키체인을 통해(이 부분은 끄지 않는 한 켜져 있습니다), 색상·테마·미터 이름·잠금 화면 배치는 본인의 iCloud를 통해 오갑니다. 1.8.7부터는 사용량 기록도 함께 옮겨 다닐 수 있어, 새 기기나 초기화한 기기가 다른 기기의 기록을 이어받습니다. 제3자를 거치는 것은 없습니다.</p>
<p><strong>Gemini 웹 앱의 한도는 왜 보이지 않나요?</strong> Google이 앱에 공개하는 것은 Gemini CLI / Code Assist 할당량뿐이며, gemini.google.com 채팅의 한도는 브라우저 밖에서는 읽을 수 없습니다.</p>
<p><strong>Mac 앱은 어디 있나요?</strong> 메뉴 막대에 있습니다. 화면 위쪽의 계기판 아이콘을 찾아보세요. Dock 아이콘은 없습니다. 클릭하면 모든 미터가 열리고, 미터를 오른쪽 클릭하면 메뉴 막대 자체에 올릴 수 있습니다.</p>
<p><strong>업데이트하면 제 설정이 바뀌나요?</strong> 아니요. 테마도, 설정 마법사도, 다른 어떤 항목도 직접 사용할 때만 바뀝니다.</p>

<h2>개인정보</h2>
<p>Runlow는 데이터를 수집하지 않고 서버도 없습니다. 앱의 개인정보 페이지(설정 → 일반 → 정보 → 개인정보)에 접속하는 모든 주소와 그 이유가 적혀 있습니다. <a href="../privacy.html">개인정보 처리방침</a>도 확인해 보세요.</p>
"""

if __name__ == "__main__":
    write("en", "Runlow - Support", EN_BODY,
          "Independent app; not affiliated with Anthropic, OpenAI, Google, Cursor, GitHub or OpenRouter.")
    write("de", "Runlow – Support", DE_BODY,
          "Unabhängige App; nicht verbunden mit Anthropic, OpenAI, Google, Cursor, GitHub oder OpenRouter.")
    write("fr", "Runlow – Assistance", FR_BODY,
          "App indépendante ; sans affiliation avec Anthropic, OpenAI, Google, Cursor, GitHub ou OpenRouter.")
    write("es", "Runlow – Soporte", ES_BODY,
          "App independiente; sin afiliación con Anthropic, OpenAI, Google, Cursor, GitHub ni OpenRouter.")
    write("it", "Runlow – Assistenza", IT_BODY,
          "App indipendente; non affiliata ad Anthropic, OpenAI, Google, Cursor, GitHub o OpenRouter.")
    write("nl", "Runlow – Ondersteuning", NL_BODY,
          "Onafhankelijke app; niet verbonden met Anthropic, OpenAI, Google, Cursor, GitHub of OpenRouter.")
    write("pt-BR", "Runlow – Suporte", PT_BODY,
          "App independente; sem vínculo com Anthropic, OpenAI, Google, Cursor, GitHub ou OpenRouter.")
    write("ja", "Runlow — サポート", JA_BODY,
          "独立したアプリです。Anthropic、OpenAI、Google、Cursor、GitHub、OpenRouterとの提携関係はありません。")
    write("zh-Hans", "Runlow — 支持", ZH_BODY,
          "独立 App，与 Anthropic、OpenAI、Google、Cursor、GitHub 或 OpenRouter 无从属关系。")
    write("ko", "Runlow — 지원", KO_BODY,
          "독립적인 앱이며 Anthropic, OpenAI, Google, Cursor, GitHub, OpenRouter와 제휴 관계가 없습니다.")
