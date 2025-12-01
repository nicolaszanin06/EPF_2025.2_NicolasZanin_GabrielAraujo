% rebase('layout', title='Statistics')

<h2>Study statistics</h2>

<!-- FILTRO POR PERÍODO -->
<section style="margin-bottom: 16px; padding: 12px; border: 1px solid #ccc; border-radius: 6px;">
  <form method="get" action="/stats" style="display:flex; gap:12px; align-items:flex-end; flex-wrap:wrap;">
    <div>
      <label for="start_date">Start date:</label><br>
      <input type="date"
             id="start_date"
             name="start_date"
             value="{{stats['start_date']}}">
    </div>
    <div>
      <label for="end_date">End date:</label><br>
      <input type="date"
             id="end_date"
             name="end_date"
             value="{{stats['end_date']}}">
    </div>
    <div>
      <button type="submit" style="margin-top: 18px; padding: 6px 12px;">
        Apply filter
      </button>
    </div>
    % if stats['start_date'] or stats['end_date']:
      <div>
        <a href="/stats" style="margin-top: 18px; display:inline-block;">Clear filter</a>
      </div>
    % end
  </form>
</section>

<!-- CARDS PRINCIPAIS -->
<section style="display:flex; flex-wrap:wrap; gap:16px; margin-bottom: 20px;">

  <div style="flex:1 1 180px; padding:12px; border-radius:8px; background:#f5f5f5;">
    <h3>Total hours</h3>
    <p style="font-size: 1.6em; font-weight:bold;">
      {{stats['total_hours']}} h
    </p>
    <small>{{stats['total_minutes']}} minutes studied</small>
  </div>

  <div style="flex:1 1 180px; padding:12px; border-radius:8px; background:#f5f5f5;">
    <h3>Sessions</h3>
    <p style="font-size: 1.6em; font-weight:bold;">
      {{stats['sessions_count']}}
    </p>
    <small>in the selected period</small>
  </div>

  <div style="flex:1 1 180px; padding:12px; border-radius:8px; background:#f5f5f5;">
    <h3>Subjects</h3>
    <p style="font-size: 1.6em; font-weight:bold;">
      {{stats['subjects_count']}}
    </p>
    <small>registered for this user</small>
  </div>

  <div style="flex:1 1 180px; padding:12px; border-radius:8px; background:#f5f5f5;">
    <h3>Topics completed</h3>
    <p style="font-size: 1.6em; font-weight:bold;">
      {{stats['topics_completed']}} / {{stats['topics_total']}}
    </p>
    % if stats['topics_total'] > 0:
      % completed_pct = int((stats['topics_completed'] / stats['topics_total']) * 100)
    % else:
      % completed_pct = 0
    % end
    <div style="margin-top:4px;">
      <div style="background:#ddd; height:8px; border-radius:4px; overflow:hidden;">
        <div style="height:8px; width:{{completed_pct}}%; background:#4caf50;"></div>
      </div>
      <small>{{completed_pct}}% completed</small>
    </div>
  </div>

</section>

<!-- BARRAS POR MATÉRIA -->
<section style="margin-bottom: 24px;">
  <h3>Study time per subject</h3>

  % minutes_per_subject = stats['minutes_per_subject']
  % if not minutes_per_subject:
    <p>No study sessions found for this period.</p>
  % else:
    % max_minutes = max(minutes_per_subject.values()) if minutes_per_subject else 0

    <div style="margin-top: 8px;">
      % for subj in subjects:
        % subj_minutes = minutes_per_subject.get(subj.id, 0)
        % if max_minutes > 0:
          % width_pct = int((subj_minutes / max_minutes) * 100)
        % else:
          % width_pct = 0
        % end

        <div style="margin-bottom: 8px;">
          <div style="display:flex; justify-content:space-between;">
            <strong>{{subj.name}}</strong>
            <span>{{subj_minutes}} min</span>
          </div>
          <div style="background:#eee; height:10px; border-radius:5px; overflow:hidden;">
            <div style="height:10px; width:{{width_pct}}%; background:#2196f3;"></div>
          </div>
        </div>
      % end
    </div>
  % end
</section>

<!-- RESUMO TEXTUAL -->
<section style="margin-bottom: 16px; padding: 12px; border: 1px solid #ccc; border-radius: 6px;">
  <h3>Summary</h3>
  % if stats['sessions_count'] == 0:
    <p>No study sessions were found for the selected period.</p>
  % else:
    <p>
      You studied a total of <strong>{{stats['total_hours']}} hours</strong>
      ({{stats['total_minutes']}} minutes) in
      <strong>{{stats['sessions_count']}} sessions</strong>.
    </p>
    % if stats['topics_total'] > 0:
      <p>
        From {{stats['topics_total']}} topics,
        <strong>{{stats['topics_completed']}}</strong> are marked as completed.
      </p>
    % end
  % end
</section>
