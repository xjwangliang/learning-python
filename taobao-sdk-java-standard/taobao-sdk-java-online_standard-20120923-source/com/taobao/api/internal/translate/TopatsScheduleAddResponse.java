package com.taobao.api.internal.translate;

import java.util.Date;
import com.taobao.api.internal.mapping.ApiField;

import com.taobao.api.TaobaoResponse;

/**
 * TOP API: taobao.topats.schedule.add response.
 * 
 * @author auto create
 * @since 1.0, null
 */
public class TopatsScheduleAddResponse extends TaobaoResponse {

	private static final long serialVersionUID = 5788818741119374931L;

	/** 
	 * 创建时间
	 */
	@ApiField("created")
	private Date created;

	/** 
	 * 任务ID
	 */
	@ApiField("task_id")
	private Long taskId;

	public void setCreated(Date created) {
		this.created = created;
	}
	public Date getCreated( ) {
		return this.created;
	}

	public void setTaskId(Long taskId) {
		this.taskId = taskId;
	}
	public Long getTaskId( ) {
		return this.taskId;
	}
}
