TEMPLATES_DICT = {
    "polls/index.html": """{% load static %}
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bilgisayar Anketi</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <!-- Core Stylesheet -->
    <link href="{% static 'polls/cyber_theme.css' %}" rel="stylesheet">
</head>
<body>
    <div class="bg-gradient-animated"></div>
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>

    <!-- Floating Background Images to make it eye-catching -->
    <img src="{% static 'polls/images/cyberpunk_gaming_pc_1774897043698.png' %}" class="floating-img img-idx-1" alt="Decor Image 1">
    <img src="{% static 'polls/images/gpu_motherboard_1774897067504.png' %}" class="floating-img img-idx-2" alt="Decor Image 2">
    <img src="{% static 'polls/images/neon_keyboard_cyber_1774899740672.png' %}" class="floating-img img-idx-3" alt="Decor Image 3">
    <img src="{% static 'polls/images/cyber_vr_headset_1774899755737.png' %}" class="floating-img img-idx-4" alt="Decor Image 4">
    <img src="{% static 'polls/images/cyber_server_room_1774900053778.png' %}" class="floating-img img-idx-5" alt="Decor Image 5">
    <img src="{% static 'polls/images/cyber_gaming_mouse_1774900068510.png' %}" class="floating-img img-idx-6" alt="Decor Image 6">

    <div class="content-wrapper">
        <!-- Component: Navigation Bar -->
        <nav class="navbar-cyber">
            <div class="container d-flex justify-content-between align-items-center">
                <a href="{% url 'polls:index' %}" class="navbar-brand-cyber">
                    <span class="brand-icon"><i class="bi bi-pc-display-horizontal"></i></span>
                    Bilgisayar Anketi
                </a>
                <div class="d-flex align-items-center">
                    <a href="{% url 'polls:add_poll' %}" class="btn btn-sm me-2" style="background: var(--glass); border: 1px solid var(--neon-blue); color: var(--neon-blue); margin-right: 10px; border-radius: 50px; padding: 0.4rem 1rem; font-size: 0.8rem;">
                        <i class="bi bi-plus-circle me-1"></i> Anket Ekle
                    </a>
                    <a href="#" class="btn btn-sm" style="background: var(--glass); border: 1px solid var(--glass-border); color: var(--accent); border-radius: 50px; padding: 0.4rem 1rem; font-size: 0.8rem; margin-right: 10px;">
                        <i class="bi bi-person-circle me-1"></i> Profil
                    </a>
                    <form action="{% url 'logout' %}" method="post" class="d-inline">
                        {% csrf_token %}
                        <button type="submit" class="btn btn-sm" style="background: var(--glass); border: 1px solid var(--glass-border); color: var(--neon-pink); border-radius: 50px; padding: 0.4rem 1rem; font-size: 0.8rem;">
                            <i class="bi bi-box-arrow-right me-1"></i> Çıkış Yap
                        </button>
                    </form>
                </div>
            </div>
        </nav>

        <!-- Component: Hero Section -->
        <div class="hero">
            <div class="hero-badge">
                <span class="pulse-dot"></span>
                Aktif Anketler
            </div>
            <h1>Bilgisayar Anket Merkezi</h1>
            <p>Bilgisayar kullanım alışkanlıklarınızı, donanım tercihlerinizi ve favori yazılımlarınızı paylaşarak PC dünyasının nabzını tutun.</p>
            
            <!-- Component: Search Bar -->
            <div class="search-container mt-4">
                <form action="{% url 'polls:index' %}" method="get" class="search-form">
                    <div class="input-group-cyber">
                        <i class="bi bi-search search-icon"></i>
                        <input type="text" name="q" value="{{ search_query }}" placeholder="Anketlerde ara..." class="form-control-cyber">
                        {% if search_query %}
                            <a href="{% url 'polls:index' %}" class="clear-search"><i class="bi bi-x-lg"></i></a>
                        {% endif %}
                        <button type="submit" class="btn-cyber">Ara</button>
                    </div>
                </form>
            </div>
        </div>

        <!-- Component: Statistics Overview -->
        <div class="stats-bar">
            <div class="stat-item">
                <div class="stat-number" id="anketSayisi">0</div>
                <div class="stat-label">Aktif Anket</div>
            </div>
            <div class="stat-item">
                <div class="stat-number" id="katilimci">0</div>
                <div class="stat-label">Katılımcı</div>
            </div>
            <div class="stat-item">
                <div class="stat-number" id="tamamlanan">0</div>
                <div class="stat-label">Tamamlanan</div>
            </div>
        </div>

        <!-- Component: Active Polls Grid -->
        <div class="container">
            {% if latest_question_list %}
                <div class="cards-grid">
                {% for question in latest_question_list %}
                    <a href="{% url 'polls:detail' question.id %}" class="poll-card" style="animation-delay: {{ forloop.counter0 }}00ms;">
                        <div class="card-icon">
                            {% if question.category %}
                                <i class="bi {{ question.category.icon }}"></i>
                            {% else %}
                                <i class="bi bi-motherboard-fill"></i>
                            {% endif %}
                        </div>
                        <div class="card-badges">
                            {% if question.category %}
                                <span class="badge-category">{{ question.category.name }}</span>
                            {% endif %}
                            {% if question.views > 10 %}
                                <span class="badge-trending"><i class="bi bi-fire me-1"></i>Popüler</span>
                            {% endif %}
                        </div>
                        <h3>{{ question.question_text }}</h3>
                        <p class="card-desc">Bu ankete katılarak kişisel donanım ve yazılım tercihlerinizi bizimle paylaşın.</p>
                        <div class="card-footer-custom">
                            <span class="card-tag"><i class="bi bi-eye-fill me-1"></i>{{ question.views }} İzlenme</span>
                            <span class="card-arrow"><i class="bi bi-arrow-right"></i></span>
                        </div>
                    </a>
                {% endfor %}
                </div>
            {% else %}
                <div class="empty-state">
                    <i class="bi bi-inbox"></i>
                    <p>Şu anda aktif bir PC/Bilgisayar anketi bulunmamaktadır.</p>
                </div>
            {% endif %}
        </div>
    </div>

    <script>
        /**
         * Animates a numerical counter from 0 to the target value.
         * @param {HTMLElement} el - The DOM element to update.
         * @param {number} target - The final number to reach.
         * @param {number} duration - Animation duration in milliseconds.
         */
        function animateCounter(el, target, duration = 2000) {
            let start = 0;
            const step = timestamp => {
                if (!start) start = timestamp;
                const progress = Math.min((timestamp - start) / duration, 1);
                el.textContent = Math.floor(progress * target);
                if (progress < 1) requestAnimationFrame(step);
            };
            requestAnimationFrame(step);
        }

        /**
         * Intersection Observer to trigger card animations when they enter the viewport.
         */
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.animationPlayState = 'running';
                }
            });
        }, { threshold: 0.1 });

        document.querySelectorAll('.poll-card').forEach(card => {
            card.style.animationPlayState = 'paused';
            observer.observe(card);
        });

        /**
         * Initializes animations once the window has fully loaded.
         */
        window.addEventListener('load', () => {
            const anketCount = {{ latest_question_list|length }};
            animateCounter(document.getElementById('anketSayisi'), anketCount, 1500);
            animateCounter(document.getElementById('katilimci'), {{ total_votes_all|default:0 }}, 2000);
            animateCounter(document.getElementById('tamamlanan'), {{ completed_polls_count|default:0 }}, 1800);
        });

        /**
         * Adds a parallax effect to floating background orbs based on mouse movement.
         * @param {MouseEvent} e - The mousemove event object.
         */
        document.addEventListener('mousemove', (e) => {
            const x = e.clientX / window.innerWidth - 0.5;
            const y = e.clientY / window.innerHeight - 0.5;
            document.querySelectorAll('.orb').forEach((orb, i) => {
                const speed = (i + 1) * 15;
                orb.style.transform += ` translate(${x * speed}px, ${y * speed}px)`;
            });
        });
    </script>
</body>
</html>
""",
    "polls/detail.html": """{% load static %}
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Anket: {{ question.question_text }} — Bilgisayar Anketi</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <!-- Core Stylesheet -->
    <link href="{% static 'polls/cyber_theme.css' %}" rel="stylesheet">
</head>
<body>
    <div class="bg-gradient-animated"></div>
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>

    <div class="content-wrapper">
        <nav class="navbar-cyber">
            <div class="container d-flex justify-content-between align-items-center">
                <a href="{% url 'polls:index' %}" class="navbar-brand-cyber">
                    <span class="brand-icon"><i class="bi bi-pc-display-horizontal"></i></span>
                    Bilgisayar Anketi
                </a>
            </div>
        </nav>

        <div class="detail-wrapper">
            <a href="{% url 'polls:index' %}" class="back-link">
                <i class="bi bi-arrow-left"></i> Tüm Anketlere Dön
            </a>

            <div class="question-card">
                <div class="question-header">
                    <div class="q-icon">
                        {% if question.category %}
                            <i class="bi {{ question.category.icon }}"></i>
                        {% else %}
                            <i class="bi bi-motherboard"></i>
                        {% endif %}
                    </div>
                    <div class="w-100">
                        <div class="d-flex justify-content-between align-items-start">
                            <h1>{{ question.question_text }}</h1>
                            <div class="detail-stats text-end">
                                {% if question.category %}
                                    <span class="badge-category d-block mb-1">{{ question.category.name }}</span>
                                {% endif %}
                                <span class="view-count" style="font-size: 0.8rem; color: var(--text-secondary);">
                                    <i class="bi bi-eye-fill"></i> {{ question.views }} İzlenme
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="question-body">
                    <form action="{% url 'polls:vote' question.id %}" method="post">
                        {% csrf_token %}
                        <span class="section-label">Seçenekler</span>

                        {% if error_message %}
                            <div class="error-msg">
                                <i class="bi bi-exclamation-triangle-fill"></i>
                                {{ error_message }}
                            </div>
                        {% endif %}

                        <ul class="choices-list">
                        {% for choice in question.choice_set.all %}
                            <li class="choice-item">
                                <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
                                <label for="choice{{ forloop.counter }}">
                                    <span class="radio-dot"></span>
                                    {{ choice.choice_text }}
                                </label>
                            </li>
                        {% endfor %}
                        </ul>

                        <div class="text-end">
                            <button type="submit" class="submit-btn">
                                Görüşümü Kaydet <i class="bi bi-send-fill"></i>
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <script>
        /**
         * Attaches a ripple effect to choice selection labels for enhanced user interaction.
         */
        document.querySelectorAll('.choice-item label').forEach(label => {
            label.addEventListener('click', function(e) {
                const ripple = document.createElement('span');
                ripple.style.cssText = `position:absolute;border-radius:50%;background:rgba(99,102,241,0.3);transform:scale(0);animation:ripple 0.6s ease-out;pointer-events:none;width:100px;height:100px;left:${e.offsetX-50}px;top:${e.offsetY-50}px;`;
                this.closest('.choice-item').style.position = 'relative';
                this.closest('.choice-item').style.overflow = 'hidden';
                this.closest('.choice-item').appendChild(ripple);
                setTimeout(() => ripple.remove(), 600);
            });
        });

        /**
         * Dynamically injects the ripple animation keyframes into the document head.
         */
        const style = document.createElement('style');
        style.textContent = '@keyframes ripple { to { transform: scale(4); opacity: 0; } }';
        document.head.appendChild(style);
    </script>
</body>
</html>
""",
    "polls/results.html": """{% load static %}
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sonuçlar: {{ question.question_text }} — Bilgisayar Anketi</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <!-- Core Stylesheet -->
    <link href="{% static 'polls/cyber_theme.css' %}" rel="stylesheet">
</head>
<body>
    <div class="bg-gradient-animated"></div>
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>

    <div class="content-wrapper">
        <nav class="navbar-cyber">
            <div class="container d-flex justify-content-between align-items-center">
                <a href="{% url 'polls:index' %}" class="navbar-brand-cyber">
                    <span class="brand-icon"><i class="bi bi-pc-display-horizontal"></i></span>
                    Bilgisayar Anketi
                </a>
            </div>
        </nav>

        <div class="results-wrapper">
            <!-- Component: Navigation Back Link -->
            <a href="{% url 'polls:index' %}" class="back-link">
                <i class="bi bi-arrow-left"></i> Tüm Anketlere Dön
            </a>

            <div class="results-card">
                <div class="results-header">
                    <div class="r-icon">
                        {% if question.category %}
                            <i class="bi {{ question.category.icon }}"></i>
                        {% else %}
                            <i class="bi bi-bar-chart-fill"></i>
                        {% endif %}
                    </div>
                    <div>
                        <div class="d-flex align-items-center gap-2 mb-1">
                            <h1 class="mb-0">Oylama Sonuçları</h1>
                            {% if question.category %}
                                <span class="badge-category">{{ question.category.name }}</span>
                            {% endif %}
                        </div>
                        <p class="subtitle">{{ question.question_text }}</p>
                    </div>
                </div>
                <div class="results-body">
                    {% for choice in sorted_choices %}
                        <div class="result-row {% if choice.votes == sorted_choices.0.votes and total_votes > 0 %}winner{% endif %}" style="animation-delay: {{ forloop.counter0 }}50ms;" data-percentage="{{ choice.percentage }}">
                            <div class="result-top">
                                <span class="result-label">
                                    {{ choice.choice_text }}
                                    {% if choice.votes == sorted_choices.0.votes and total_votes > 0 %}<span class="winner-badge"><i class="bi bi-trophy-fill me-1"></i>1. Sıra</span>{% endif %}
                                </span>
                                <span class="result-votes">{{ choice.votes }} oy</span>
                            </div>
                            <div class="progress-bar-custom">
                                <div class="progress-fill"></div>
                            </div>
                            <div class="result-pct">%{{ choice.percentage|floatformat:1 }}</div>
                        </div>
                    {% endfor %}

                    <div class="summary-bar">
                        <div class="total-info">
                            <div class="t-icon"><i class="bi bi-people-fill"></i></div>
                            <div>
                                <div class="total-label">Toplam Katılım</div>
                                <div class="total-number" id="totalCounter">0</div>
                            </div>
                        </div>
                        <a href="{% url 'polls:detail' question.id %}" class="vote-again-btn">
                            <i class="bi bi-arrow-clockwise"></i> Tekrar Oyla
                        </a>
                    </div>
                    
                    <!-- Navigation Buttons -->
                    <div class="d-flex justify-content-between align-items-center mt-4 pt-4" style="border-top: 1px solid var(--glass-border);">
                        {% if prev_question %}
                            <a href="{% url 'polls:detail' prev_question.id %}" class="btn btn-sm btn-outline-cyber d-inline-block w-auto px-3" style="border-radius: 8px;">
                                <i class="bi bi-arrow-left mt-1 me-1"></i> Geri
                            </a>
                        {% else %}
                            <span class="btn btn-sm btn-outline-cyber d-inline-block w-auto px-3 disabled" style="opacity: 0.3; border-radius: 8px; cursor: not-allowed;">
                                <i class="bi bi-arrow-left mt-1 me-1"></i> Geri
                            </span>
                        {% endif %}

                        <a href="{% url 'polls:index' %}" class="btn btn-sm btn-cyber d-inline-block w-auto px-4 py-2" style="border-radius: 50px; text-decoration: none;">
                            <i class="bi bi-house-door-fill me-1"></i> Ana Menü
                        </a>

                        {% if next_question %}
                            <a href="{% url 'polls:detail' next_question.id %}" class="btn btn-sm btn-outline-cyber d-inline-block w-auto px-3" style="border-radius: 8px;">
                                İleri <i class="bi bi-arrow-right mt-1 ms-1"></i>
                            </a>
                        {% else %}
                            <span class="btn btn-sm btn-outline-cyber d-inline-block w-auto px-3 disabled" style="opacity: 0.3; border-radius: 8px; cursor: not-allowed;">
                                İleri <i class="bi bi-arrow-right mt-1 ms-1"></i>
                            </span>
                        {% endif %}
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        /**
         * Animates the result progress bars and counters sequentially upon page load.
         */
        window.addEventListener('load', () => {
            setTimeout(() => {
                document.querySelectorAll('.result-row').forEach(row => {
                    const pct = row.dataset.percentage;
                    const fill = row.querySelector('.progress-fill');
                    if (fill) fill.style.width = pct + '%';
                });
            }, 300);

            /**
             * Internal function to animate the total participation counter element.
             */
            const totalEl = document.getElementById('totalCounter');
            const target = {{ total_votes }};
            let start = 0;
            const duration = 1500;
            const step = (ts) => {
                if (!start) start = ts;
                const progress = Math.min((ts - start) / duration, 1);
                totalEl.textContent = Math.floor(progress * target);
                if (progress < 1) requestAnimationFrame(step);
            };
            requestAnimationFrame(step);
        });

        /**
         * Initiates a celebratory confetti burst effect if participation exists.
         */
        {% if total_votes > 0 %}
        window.addEventListener('load', () => {
            setTimeout(() => {
                for (let i = 0; i < 30; i++) {
                    const confetti = document.createElement('div');
                    const colors = ['#6366f1','#06b6d4','#22c55e','#f59e0b','#ef4444','#8b5cf6'];
                    const color = colors[Math.floor(Math.random() * colors.length)];
                    confetti.style.cssText = `
                        position: fixed; width: 8px; height: 8px; background: ${color};
                        left: ${Math.random() * 100}vw; top: -10px; border-radius: ${Math.random() > 0.5 ? '50%' : '2px'};
                        z-index: 9999; pointer-events: none;
                        animation: confettiFall ${2 + Math.random() * 2}s ease-in forwards;
                        animation-delay: ${Math.random() * 0.5}s;
                    `;
                    document.body.appendChild(confetti);
                    setTimeout(() => confetti.remove(), 5000);
                }
            }, 800);
        });

        const confettiStyle = document.createElement('style');
        confettiStyle.textContent = `
            @keyframes confettiFall {
                0% { transform: translateY(0) rotate(0deg); opacity: 1; }
                100% { transform: translateY(100vh) rotate(720deg); opacity: 0; }
            }
        `;
        document.head.appendChild(confettiStyle);
        {% endif %}
    </script>
</body>
</html>
""",
    "polls/add_poll.html": """{% load static %}
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yeni Anket Ekle | Bilgisayar Anketi</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Orbitron:wght@400;500;700;900&display=swap" rel="stylesheet">
    <link href="{% static 'polls/cyber_theme.css' %}" rel="stylesheet">
    <style>
        .login-wrapper {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: calc(100vh - 80px);
            padding: 2rem;
            position: relative;
        }

        .login-card {
            background: var(--glass);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: 1.5rem;
            padding: 3rem;
            width: 100%;
            max-width: 600px;
            z-index: 10;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            animation: fadeInUp 0.8s ease;
        }

        .brand-header { text-align: center; margin-bottom: 2rem; }
        .brand-icon-lg {
            font-size: 3rem;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
            display: inline-block;
            filter: drop-shadow(0 0 10px rgba(244, 63, 94, 0.3));
        }

        .brand-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.6rem;
            font-weight: 700;
            color: var(--text-primary);
        }

        .cyber-form input, .cyber-form select {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--glass-border);
            color: var(--text-primary);
            border-radius: 12px;
            padding: 0.8rem 1.25rem;
            width: 100%;
            font-size: 1rem;
            transition: all 0.3s ease;
        }
        
        .cyber-form select option {
            color: #000;
            background: #fff;
        }

        .cyber-form input:focus, .cyber-form select:focus {
            background: rgba(255, 255, 255, 0.06);
            border-color: var(--primary);
            box-shadow: 0 0 0 4px rgba(244, 63, 94, 0.1);
            outline: none;
        }

        .error-message {
            background: rgba(239, 68, 68, 0.1);
            border: 1px solid rgba(239, 68, 68, 0.3);
            color: #fca5a5;
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 1.5rem;
        }

        .btn-outline-cyber {
            border: 1px solid var(--primary-light);
            color: var(--primary-light);
            border-radius: 12px;
            font-weight: 600;
            padding: 0.6rem 1rem;
            transition: all 0.3s ease;
        }
        .btn-outline-cyber:hover {
            background: rgba(244, 63, 94, 0.1);
            color: var(--text-primary);
        }
    </style>
</head>
<body>
    <div class="bg-gradient-animated"></div>
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>

    <!-- Floating Background Decor Images -->
    <img src="{% static 'polls/images/neon_keyboard_cyber_1774899740672.png' %}" class="floating-img img-idx-1" alt="Keyboard Decor" style="top: 20%; left: 3%;">
    <img src="{% static 'polls/images/cyber_vr_headset_1774899755737.png' %}" class="floating-img img-idx-2" alt="VR Headset" style="top: 45%; right: 3%;">

    <div class="content-wrapper">
        <nav class="navbar-cyber">
            <div class="container d-flex justify-content-between align-items-center">
                <a href="{% url 'polls:index' %}" class="navbar-brand-cyber">
                    <span class="brand-icon"><i class="bi bi-pc-display-horizontal"></i></span>
                    Bilgisayar Anketi
                </a>
            </div>
        </nav>

        <div class="login-wrapper">
            <div class="login-card">
                <div class="brand-header">
                    <div class="brand-icon-lg">
                        <i class="bi bi-patch-question-fill"></i>
                    </div>
                    <h1 class="brand-title">Yeni Anket Ekle</h1>
                </div>

                {% if error_message %}
                <div class="error-message collapse show text-center" style="font-size: 0.9rem;">
                    <i class="bi bi-exclamation-triangle-fill"></i> {{ error_message }}
                </div>
                {% endif %}

                <form method="post" action="{% url 'polls:add_poll' %}" class="cyber-form">
                    {% csrf_token %}
                    
                    <div class="mb-4">
                        <label class="form-label text-secondary mb-2" style="font-size: 0.9rem;">Anket Sorusu</label>
                        <input type="text" name="question_text" value="{{ question_text|default:'' }}" required placeholder="Örn: En sevdiğiniz anti-virüs programı hangisi?">
                    </div>

                    <div class="mb-4">
                        <label class="form-label text-secondary mb-2" style="font-size: 0.9rem;">Kategori (İsteğe Bağlı)</label>
                        <select name="category">
                            <option value="">-- Kategori Seçin --</option>
                            {% for c in categories %}
                                <option value="{{ c.id }}">{{ c.name }}</option>
                            {% endfor %}
                        </select>
                    </div>

                    <div id="choices-container">
                        <label class="form-label text-secondary mb-2" style="font-size: 0.9rem;">Şıklar (En az 2 şık gerekli)</label>
                        <div class="mb-3">
                            <input type="text" name="choice_1" required placeholder="1. Seçenek (Şık)">
                        </div>
                        <div class="mb-3">
                            <input type="text" name="choice_2" required placeholder="2. Seçenek (Şık)">
                        </div>
                    </div>

                    <div class="mb-4 text-start">
                        <button type="button" class="btn btn-sm btn-outline-cyber btn-add-choice">
                            <i class="bi bi-plus-circle me-1"></i> Yeni Şık Ekle
                        </button>
                    </div>

                    <button type="submit" class="btn-cyber w-100" style="padding: 1rem; border-radius: 12px; font-size: 1.1rem; display: flex; justify-content: center; align-items: center; gap: 0.5rem; font-family: 'Orbitron', sans-serif;">
                        Anketi Yayınla <i class="bi bi-cloud-arrow-up-fill ms-2"></i>
                    </button>
                    
                    <div class="text-center mt-3">
                        <a href="{% url 'polls:index' %}" class="text-secondary text-decoration-none" style="font-size: 0.8rem;">
                            <i class="bi bi-x-circle me-1"></i> İptal Et ve Geri Dön
                        </a>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const container = document.getElementById('choices-container');
            const addBtn = document.querySelector('.btn-add-choice');
            let choiceCount = 2;

            addBtn.addEventListener('click', () => {
                if (choiceCount >= 10) {
                    alert("Bir ankete en fazla 10 şık ekleyebilirsiniz.");
                    return;
                }
                choiceCount++;
                const div = document.createElement('div');
                div.className = 'mb-3';
                div.innerHTML = `<input type="text" name="choice_${choiceCount}" required placeholder="${choiceCount}. Seçenek (Şık)" style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--glass-border); color: var(--text-primary); border-radius: 12px; padding: 0.8rem 1.25rem; width: 100%; font-size: 1rem; transition: all 0.3s ease;">`;
                container.appendChild(div);
                
                // Add focus style listeners since we are appending raw html without CSS classes binding explicitly to pseudo elements sometimes
                const input = div.querySelector('input');
                input.addEventListener('focus', function() {
                    this.style.borderColor = 'var(--primary)';
                    this.style.boxShadow = '0 0 0 4px rgba(244, 63, 94, 0.1)';
                    this.style.background = 'rgba(255, 255, 255, 0.06)';
                });
                input.addEventListener('blur', function() {
                    this.style.borderColor = 'var(--glass-border)';
                    this.style.boxShadow = 'none';
                    this.style.background = 'rgba(255, 255, 255, 0.03)';
                });
            });
        });
    </script>
</body>
</html>
""",
    "registration/login.html": """{% load static %}
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bilgisayar Anketi | Giriş Yap</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Orbitron:wght@400;500;700;900&display=swap" rel="stylesheet">
    <link href="{% static 'polls/cyber_theme.css' %}" rel="stylesheet">
    <style>
        .login-wrapper {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: calc(100vh - 80px); /* minus navbar */
            padding: 2rem;
            position: relative;
        }

        .login-card {
            background: var(--glass);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: 1.5rem;
            padding: 3rem;
            width: 100%;
            max-width: 450px;
            z-index: 10;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            animation: fadeInUp 0.8s ease;
        }

        .brand-header {
            text-align: center;
            margin-bottom: 2.5rem;
        }

        .brand-icon-lg {
            font-size: 3.5rem;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
            display: inline-block;
            filter: drop-shadow(0 0 10px rgba(244, 63, 94, 0.3));
        }

        .brand-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.8rem;
            font-weight: 700;
            letter-spacing: 1px;
            margin: 0;
            color: var(--text-primary);
        }

        .brand-subtitle {
            color: var(--text-secondary);
            font-size: 1rem;
            margin-top: 0.5rem;
            font-weight: 500;
        }

        /* Form Controls */
        .form-floating > .form-control {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--glass-border);
            color: var(--text-primary);
            border-radius: 12px;
            padding: 1rem 1.25rem;
            height: auto;
            font-size: 1rem;
            transition: all 0.3s ease;
        }

        .form-floating > .form-control:focus {
            background: rgba(255, 255, 255, 0.06);
            border-color: var(--primary);
            box-shadow: 0 0 0 4px rgba(244, 63, 94, 0.1);
        }

        .form-floating > label {
            color: var(--text-secondary);
            padding: 1rem 1.25rem;
        }

        .form-floating > .form-control:focus ~ label,
        .form-floating > .form-control:not(:placeholder-shown) ~ label {
            color: var(--primary);
            transform: scale(0.85) translateY(-1.2rem) translateX(0.15rem);
            background: transparent;
        }

        .input-icon {
            position: absolute;
            right: 1.25rem;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-secondary);
            font-size: 1.2rem;
            pointer-events: none;
            transition: color 0.3s ease;
        }

        .form-control:focus + .input-icon {
            color: var(--primary);
        }

        .error-message {
            background: rgba(239, 68, 68, 0.1);
            border: 1px solid rgba(239, 68, 68, 0.3);
            color: #fca5a5;
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 1.5rem;
            font-size: 0.95rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .btn-outline-cyber {
            border: 1px solid var(--primary-light);
            color: var(--primary-light);
            border-radius: 12px;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            padding: 0.8rem;
            width: 100%;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
            text-align: center;
        }

        .btn-outline-cyber:hover {
            background: rgba(244, 63, 94, 0.1);
            color: var(--text-primary);
            box-shadow: 0 0 15px rgba(244, 63, 94, 0.4);
        }

        .auth-divider {
            margin: 2rem 0;
            display: flex;
            align-items: center;
            text-align: center;
            color: var(--text-secondary);
            font-size: 0.85rem;
        }
        .auth-divider::before, .auth-divider::after {
            content: '';
            flex: 1;
            border-bottom: 1px solid var(--glass-border);
        }
        .auth-divider span {
            padding: 0 10px;
        }
        
    </style>
</head>
<body>
    <div class="bg-gradient-animated"></div>
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>

    <!-- Floating Background Images -->
    <img src="{% static 'polls/images/cyberpunk_gaming_pc_1774897043698.png' %}" class="floating-img img-idx-1" alt="Decor Image 1">
    <img src="{% static 'polls/images/gpu_motherboard_1774897067504.png' %}" class="floating-img img-idx-2" alt="Decor Image 2">

    <div class="content-wrapper">
        <nav class="navbar-cyber">
            <div class="container d-flex justify-content-between align-items-center">
                <a href="{% url 'polls:index' %}" class="navbar-brand-cyber">
                    <span class="brand-icon"><i class="bi bi-pc-display-horizontal"></i></span>
                    Bilgisayar Anketi
                </a>
            </div>
        </nav>

        <div class="login-wrapper">
            <div class="login-card">
                <div class="brand-header">
                    <div class="brand-icon-lg">
                        <i class="bi bi-pc-display-horizontal"></i>
                    </div>
                    <h1 class="brand-title">Sisteme Giriş</h1>
                    <p class="brand-subtitle">Anketlere katılmak için giriş yapın</p>
                </div>

                {% if form.errors %}
                <div class="error-message">
                    <i class="bi bi-exclamation-triangle"></i>
                    Kullanıcı adı veya şifre hatalı. Lütfen tekrar deneyin.
                </div>
                {% endif %}

                <form method="post" action="{% url 'login' %}">
                    {% csrf_token %}
                    
                    <div class="form-floating mb-4 position-relative">
                        <input type="text" class="form-control" id="username" name="username" placeholder="Kullanıcı Adı" required autofocus>
                        <i class="bi bi-person input-icon"></i>
                        <label for="username">Kullanıcı Adı</label>
                    </div>

                    <div class="form-floating mb-4 position-relative">
                        <input type="password" class="form-control" id="password" name="password" placeholder="Şifre" required>
                        <i class="bi bi-key input-icon"></i>
                        <label for="password">Şifre</label>
                    </div>

                    <button type="submit" class="btn-cyber w-100" style="padding: 1rem; border-radius: 12px; font-size: 1.1rem; display: flex; justify-content: center; align-items: center; gap: 0.5rem; font-family: 'Orbitron', sans-serif;">
                        Bağlan <i class="bi bi-box-arrow-in-right"></i>
                    </button>
                    <input type="hidden" name="next" value="{{ next|default:'/polls/' }}">
                </form>

                <div class="auth-divider">
                    <span>VEYA</span>
                </div>

                <div class="text-center">
                    <a href="{% url 'signup' %}" class="btn-outline-cyber">
                        Yeni Hesap Oluştur <i class="bi bi-person-plus ms-2"></i>
                    </a>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
""",
    "registration/signup.html": """{% load static %}
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bilgisayar Anketi | Kayıt Ol</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Orbitron:wght@400;500;700;900&display=swap" rel="stylesheet">
    <link href="{% static 'polls/cyber_theme.css' %}" rel="stylesheet">
    <style>
        .login-wrapper {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: calc(100vh - 80px);
            padding: 2rem;
            position: relative;
        }

        .login-card {
            background: var(--glass);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: 1.5rem;
            padding: 3rem;
            width: 100%;
            max-width: 500px; /* Slightly wider for signup form */
            z-index: 10;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            animation: fadeInUp 0.8s ease;
        }

        .brand-header {
            text-align: center;
            margin-bottom: 2rem;
        }

        .brand-icon-lg {
            font-size: 3rem;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
            display: inline-block;
            filter: drop-shadow(0 0 10px rgba(244, 63, 94, 0.3));
        }

        .brand-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.6rem;
            font-weight: 700;
            letter-spacing: 1px;
            margin: 0;
            color: var(--text-primary);
        }

        .brand-subtitle {
            color: var(--text-secondary);
            font-size: 0.95rem;
            margin-top: 0.5rem;
            font-weight: 500;
        }

        /* Form Controls customized for UserCreationForm */
        .cyber-form input {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--glass-border);
            color: var(--text-primary);
            border-radius: 12px;
            padding: 0.8rem 1.25rem;
            width: 100%;
            font-size: 1rem;
            transition: all 0.3s ease;
        }

        .cyber-form input:focus {
            background: rgba(255, 255, 255, 0.06);
            border-color: var(--primary);
            box-shadow: 0 0 0 4px rgba(244, 63, 94, 0.1);
            outline: none;
        }

        .cyber-form ul.errorlist {
            list-style: none;
            padding-left: 0;
            margin-top: 0.5rem;
            color: #fca5a5;
            font-size: 0.85rem;
        }

        .btn-outline-cyber {
            border: 1px solid var(--primary-light);
            color: var(--primary-light);
            border-radius: 12px;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            padding: 0.8rem;
            width: 100%;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
            text-align: center;
        }

        .btn-outline-cyber:hover {
            background: rgba(244, 63, 94, 0.1);
            color: var(--text-primary);
            box-shadow: 0 0 15px rgba(244, 63, 94, 0.4);
        }

        .auth-divider {
            margin: 2rem 0;
            display: flex;
            align-items: center;
            text-align: center;
            color: var(--text-secondary);
            font-size: 0.85rem;
        }
        .auth-divider::before, .auth-divider::after {
            content: '';
            flex: 1;
            border-bottom: 1px solid var(--glass-border);
        }
        .auth-divider span {
            padding: 0 10px;
        }

        /* btn-cyber inherited from cyber_theme but redefining for standalone */
        .btn-cyber-submit {
            background: linear-gradient(135deg, var(--primary) 0%, #7c3aed 100%);
            border: none;
            color: white;
            transition: all 0.3s ease;
            box-shadow: 0 10px 20px -10px rgba(244, 63, 94, 0.5);
            padding: 1rem; 
            border-radius: 12px; 
            font-size: 1.1rem; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            gap: 0.5rem; 
            font-family: 'Orbitron', sans-serif;
            width: 100%;
        }
        
        .btn-cyber-submit:hover {
            transform: translateY(-2px);
            box-shadow: 0 15px 25px -10px rgba(244, 63, 94, 0.7);
        }
    </style>
</head>
<body>
    <div class="bg-gradient-animated"></div>
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>

    <img src="{% static 'polls/images/cyberpunk_gaming_pc_1774897043698.png' %}" class="floating-img img-idx-1" alt="Decor Image 1">
    <img src="{% static 'polls/images/gpu_motherboard_1774897067504.png' %}" class="floating-img img-idx-2" alt="Decor Image 2">

    <div class="content-wrapper">
        <nav class="navbar-cyber">
            <div class="container d-flex justify-content-between align-items-center">
                <a href="{% url 'polls:index' %}" class="navbar-brand-cyber">
                    <span class="brand-icon"><i class="bi bi-pc-display-horizontal"></i></span>
                    Bilgisayar Anketi
                </a>
            </div>
        </nav>

        <div class="login-wrapper">
            <div class="login-card">
                <div class="brand-header">
                    <div class="brand-icon-lg">
                        <i class="bi bi-person-plus-fill"></i>
                    </div>
                    <h1 class="brand-title">Yeni Kayıt</h1>
                    <p class="brand-subtitle">Anket sistemine katılmak için hesap oluşturun</p>
                </div>

                <form method="post" action="{% url 'signup' %}" class="cyber-form">
                    {% csrf_token %}
                    
                    {% for field in form %}
                    <div class="mb-3">
                        <label class="form-label" style="color: var(--text-secondary); font-size: 0.9rem;" for="{{ field.id_for_label }}">{{ field.label }}</label>
                        {{ field }}
                        {% if field.help_text %}
                        <small class="form-text mt-1 d-block" style="font-size: 0.75rem; color: var(--text-secondary); opacity: 0.8;">{{ field.help_text|safe }}</small>
                        {% endif %}
                        {% for error in field.errors %}
                        <div class="text-danger mt-1" style="font-size: 0.85rem;">{{ error }}</div>
                        {% endfor %}
                    </div>
                    {% endfor %}

                    <button type="submit" class="btn-cyber-submit mt-4">
                        Hesabımı Oluştur <i class="bi bi-person-check-fill ms-2"></i>
                    </button>
                </form>

                <div class="auth-divider">
                    <span>VEYA</span>
                </div>

                <div class="text-center">
                    <a href="{% url 'login' %}" class="btn-outline-cyber">
                        Zaten hesabım var - Giriş Yap <i class="bi bi-box-arrow-in-right ms-2"></i>
                    </a>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
""",
}
