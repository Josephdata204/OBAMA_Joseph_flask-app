from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    html = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Application Docker - Joseph</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        .stars {
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            z-index: 0;
            pointer-events: none;
        }

        .star {
            position: absolute;
            background: white;
            border-radius: 50%;
            animation: twinkle 3s infinite;
        }

        @keyframes twinkle {
            0%, 100% { opacity: 0.2; transform: scale(1); }
            50% { opacity: 1; transform: scale(1.3); }
        }

        .container {
            position: relative;
            z-index: 1;
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 24px;
            padding: 60px 50px;
            max-width: 700px;
            width: 90%;
            text-align: center;
            box-shadow: 0 25px 60px rgba(0,0,0,0.5);
            animation: fadeIn 1.2s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .docker-logo {
            font-size: 80px;
            margin-bottom: 20px;
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        h1 {
            font-size: 2.2rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 10px;
            text-shadow: 0 2px 10px rgba(100,150,255,0.5);
        }

        .subtitle {
            color: #a0b4ff;
            font-size: 1.1rem;
            margin-bottom: 40px;
        }

        .badge-row {
            display: flex;
            justify-content: center;
            gap: 12px;
            flex-wrap: wrap;
            margin-bottom: 40px;
        }

        .badge {
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.2);
            color: #e0e7ff;
            padding: 8px 18px;
            border-radius: 50px;
            font-size: 0.85rem;
            font-weight: 500;
        }

        .badge.blue { background: rgba(59,130,246,0.3); border-color: #3b82f6; }
        .badge.green { background: rgba(34,197,94,0.3); border-color: #22c55e; }
        .badge.purple { background: rgba(168,85,247,0.3); border-color: #a855f7; }

        .info-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin-bottom: 40px;
        }

        .info-card {
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 14px;
            padding: 20px 16px;
            transition: transform 0.3s, background 0.3s;
        }

        .info-card:hover {
            transform: translateY(-4px);
            background: rgba(255,255,255,0.1);
        }

        .info-card .icon { font-size: 2rem; margin-bottom: 8px; }
        .info-card .label { color: #94a3b8; font-size: 0.8rem; margin-bottom: 4px; }
        .info-card .value { color: #e2e8f0; font-size: 1rem; font-weight: 600; }

        .status {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(34,197,94,0.15);
            border: 1px solid rgba(34,197,94,0.4);
            color: #4ade80;
            padding: 12px 28px;
            border-radius: 50px;
            font-weight: 600;
            font-size: 1rem;
        }

        .pulse {
            width: 10px; height: 10px;
            background: #4ade80;
            border-radius: 50%;
            animation: pulse 1.5s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); box-shadow: 0 0 0 0 rgba(74,222,128,0.5); }
            50% { opacity: 0.7; transform: scale(1.2); box-shadow: 0 0 0 6px rgba(74,222,128,0); }
        }

        footer {
            margin-top: 40px;
            color: rgba(255,255,255,0.3);
            font-size: 0.8rem;
        }
    </style>
</head>
<body>
    <div class="stars" id="stars"></div>
    <div class="container">
        <div class="docker-logo">🐳</div>
        <h1>Application Conteneurisée</h1>
        <p class="subtitle">Déployée avec Docker par <strong style="color:#818cf8">Joseph</strong></p>

        <div class="badge-row">
            <span class="badge blue">🐍 Python 3.9</span>
            <span class="badge green">🚀 Flask</span>
            <span class="badge purple">🐳 Docker</span>
        </div>

        <div class="info-grid">
            <div class="info-card">
                <div class="icon">📦</div>
                <div class="label">Technologie</div>
                <div class="value">Docker Container</div>
            </div>
            <div class="info-card">
                <div class="icon">🌐</div>
                <div class="label">Port exposé</div>
                <div class="value">5000</div>
            </div>
            <div class="info-card">
                <div class="icon">🏫</div>
                <div class="label">Cours</div>
                <div class="value">Conduite de Projet</div>
            </div>
            <div class="info-card">
                <div class="icon">👤</div>
                <div class="label">Auteur</div>
                <div class="value">Joseph</div>
            </div>
        </div>

        <div class="status">
            <div class="pulse"></div>
            Conteneur en cours d'exécution
        </div>

        <footer>
            <p>TP1 Docker · CC1 Agile/DevOps/Kanban · Université de Yaoundé I</p>
        </footer>
    </div>

    <script>
        const starsContainer = document.getElementById('stars');
        for (let i = 0; i < 80; i++) {
            const star = document.createElement('div');
            star.className = 'star';
            const size = Math.random() * 3 + 1;
            star.style.cssText = `
                width: ${size}px; height: ${size}px;
                top: ${Math.random() * 100}%;
                left: ${Math.random() * 100}%;
                animation-delay: ${Math.random() * 3}s;
                animation-duration: ${2 + Math.random() * 3}s;
            `;
            starsContainer.appendChild(star);
        }
    </script>
</body>
</html>
    """
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
